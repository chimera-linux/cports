from cbuild.core import logger, paths, chroot, profile, template
from cbuild.util import flock
from cbuild.apk import cli

import time
import subprocess


# this one has the dummy root available
def check_stage(arch, force=False, remote=False):
    added = {}
    dropped = {}
    replaced = {}
    revdeps = {}

    def _call_apk(*args):
        return subprocess.run(
            [
                paths.apk(),
                "--quiet",
                "--arch",
                arch,
                "--allow-untrusted",
                "--root",
                paths.bldroot(),
                *args,
            ],
            capture_output=True,
        )

    # full repo list for revdep search
    rlist = []

    repop = paths.repository()
    stagep = paths.stage_repository()

    rs = []  # stage repos
    if remote:
        # when remote-checking, local repo is our stage, and only select ones
        stagep = repop
        for r in chroot.get_confrepos():
            if not r.startswith("/"):
                # skip remotes
                continue
            # go over allowed repos
            for sect in template.get_cats():
                rp = stagep / r.lstrip("/").replace("@section@", sect)
                rbase = rp / arch
                ridx = rbase / "Packages.adb"
                if not ridx.is_file():
                    ridx = rbase / "APKINDEX.tar.gz"
                if not ridx.is_file():
                    continue
                rs.append(ridx)
    else:
        for f in cli.find_indexes(stagep):
            if f.parent.name != arch:
                continue
            rs.append(f)
    rs.sort()

    if force:
        return rs

    rr = []  # regular repos
    rrm = {}  # mapping for stage
    if remote:
        prof = profile.get_profile(arch)
        # when remote-checking, remote repo is the regular one, only known ones
        for r in chroot.get_confrepos():
            if r.startswith("/"):
                # skip locals
                continue
            # go over known repos
            for sect in prof.repos:
                sidx = r.find("@section@")
                url = r.replace("@section@", sect)
                rr.append(url)
                if sidx > 0:
                    rrm[r[sidx:].replace("@section@", sect)] = url
    else:
        for f in cli.find_indexes(repop):
            if f.parent.name != arch:
                continue
            rr.append(f)
            rrm[str(f.parent.parent.relative_to(repop))] = f
    rr.sort()

    for r in rs:
        rlist += ["--repository", str(r)]
    for r in rr:
        rlist += ["--repository", str(r)]

    # not needed for local repos (basically a noop for those) but
    # for remote repos this is important for provider checking
    _call_apk(*rlist, "update")

    for d in rs:
        reld = str(d.relative_to(stagep).parent.parent)
        # only stage exists, so nothing is replacing anything
        ad = rrm.get(reld, None)
        if not ad:
            continue
        # search for all staged packages
        ret = _call_apk("--from", "none", "--repository", str(d), "search")
        # go over each staged package
        for p in ret.stdout.strip().decode().split():
            # stage providers
            pr = _call_apk(
                "--from",
                "none",
                "--repository",
                str(d),
                "info",
                "--provides",
                p,
            )
            stpr = set(pr.stdout.strip().decode().split())
            # repo providers
            pr = _call_apk(
                "--from",
                "none",
                "--repository",
                str(ad),
                "info",
                "--provides",
                p,
            )
            rppr = set(pr.stdout.strip().decode().split())
            # if they are the same, just skip
            if stpr == rppr:
                continue
            # accumulate stage providers
            for pr in stpr:
                vp = pr.find("=")
                if vp > 0:
                    added[pr[0:vp]] = pr[vp + 1 :]
                else:
                    added[pr] = True
            # accumulate repo providers
            for pr in rppr:
                vp = pr.find("=")
                if vp > 0:
                    dropped[pr[0:vp]] = pr[vp + 1 :]
                else:
                    dropped[pr] = True
            # track as replaced
            replaced[p] = True

    # now we have both added and dropped providers, ditch common ones
    for pk in list(added.keys()):
        if pk in dropped and dropped[pk] == added[pk]:
            del added[pk]
            del dropped[pk]

    # for each dropped provider, get known revdeps and accumulate a set
    if len(dropped) > 0:
        for pn in (
            _call_apk(
                *rlist,
                "search",
                "--from",
                "none",
                "--exact",
                "--all",
                "--rdepends",
                *list(dropped.keys()),
            )
            .stdout.strip()
            .decode()
            .split()
        ):
            revdeps[pn] = True

    # potentially missing deps
    checkdeps = {}

    # for each revdep, do a dep check using potentially staged packages
    # ensure that there is no dependency on a provider that was dropped
    # without a replacement
    for d in revdeps:
        # dependencies of the most significant (maybe staged) provider
        deps = []
        # go over each repo separately for robustness, break on first that
        # actually does contain the package (will return at least a '\n')
        for tryr in rlist:
            if tryr == "--repository":
                continue
            ret = _call_apk(
                "--repository", tryr, "info", "--from", "none", "--depends", d
            )
            if ret.returncode != 0 or len(ret.stdout) == 0:
                # does not exist in this repo
                continue
            # get a list, which may be empty
            deps = ret.stdout.strip().decode().split()
            break
        # verify each dep
        for ad in deps:
            av = None
            ao = None
            # check if versioned
            for i, c in enumerate(ad):
                # get the version and operator
                if c == "=":
                    av = ad[i + 1 :]
                    ao = c
                    ad = ad[0:i]
                    break
                elif c == "<" or c == ">":
                    if ad[i + 1 : i + 2] == "=":
                        av = ad[i + 2 :]
                        ao = c + "="
                    else:
                        av = ad[i + 1 :]
                        ao = c
                    ad = ad[0:i]
                    break
            # dependency not in dropped providers at all, skip
            if ad not in dropped:
                continue
            # if not versioned, just outright consider it
            if av is None:
                if ad in added:
                    # replacement provider was added
                    continue
                if ad in checkdeps:
                    checkdeps[ad].append(d)
                else:
                    checkdeps[ad] = [d]
            else:
                # do a constraint check for dropped
                dv = dropped[ad]
                if dv is not True:
                    ret = _call_apk("version", "--test", av, dv).stdout.strip()
                    if ret == b"<":
                        # constraint ver is lower than provider ver
                        # skip constraints that ask for a smaller/equal version
                        if ao == "=" or ao.startswith("<"):
                            continue
                    elif ret == b">":
                        # constraint ver is larger than provider ver
                        # skip constraints that ask for a larger/equal version
                        if ao == "=" or ao.startswith(">"):
                            continue
                    else:
                        # constraint ver and provider ver are the same
                        # skip constraints that ask for a larger version
                        if ao == ">":
                            continue
                # the deleted constraint matched; now check if an added matches
                nv = added.get(ad, None)
                if nv is not None:
                    ret = _call_apk("version", "--test", av, nv).stdout.strip()
                    if ret == b"<":
                        # constraint ver is lower than provider ver
                        if ao.startswith(">"):
                            continue
                    elif ret == b">":
                        # constraint ver is larger than provider ver
                        if ao.startswith("<"):
                            continue
                    else:
                        # constraint ver and provider ver are the same
                        if ao != ">":
                            continue
                # satisfied old constraints but not any new ones
                # that means it's a considered depdendency
                if ad in checkdeps:
                    checkdeps[ad].append(d)
                else:
                    checkdeps[ad] = [d]

    # if there were such cases, further narrow them down to ensure that
    # we are not dealing with something that still has another suitable
    # provider, as that should not stage us
    for d in list(checkdeps.keys()):
        ret = _call_apk(
            *rlist, "search", "--from", "none", "--all", "--exact", d
        )
        # for each provider of sketchy dependency, if it's provided
        # using a name that was not deleted, it's probably okay
        for pd in ret.stdout.strip().decode().split():
            if pd not in replaced:
                del checkdeps[d]
                break

    # we can safely unstage as there is nothing left
    if len(checkdeps) == 0:
        return rs

    if not remote:
        logger.get().out("Cannot unstage repositories:")
    else:
        logger.get().out("Unstage requirements:")

    # ensure repo remains staged
    # also print a list of stuff to rebuild and what causes
    # it to require rebuilding for informational purposes
    for d in checkdeps:
        print(f" rebuild: {', '.join(checkdeps[d])} ({d})")

    return None


def _do_clear(arch, force):
    repop = paths.repository()
    stagep = paths.stage_repository()
    log = logger.get()

    log.out(f"Clearing staged {arch} repos for {repop}...")

    unstage = check_stage(arch, force)

    # FIXME: compute from git if possible
    epoch = int(time.time())

    for d in unstage or []:
        d = d.parent.parent / arch
        ad = repop / d.relative_to(stagep)
        try:
            ad.rmdir()
        except Exception:
            pass
        # just migrate if possible, easier this way
        if not ad.is_dir():
            log.out(f"Migrating stage from {d} to {ad}...")
            ad.parent.mkdir(parents=True, exist_ok=True)
            d.rename(ad)
            continue
        # else merge the directories
        log.out(f"Merging stage from {d} to {ad}...")
        ad.mkdir(parents=True, exist_ok=True)
        for f in d.glob("*.apk"):
            f.rename(ad / f.name)
        # clear the stage index, we won't need it
        (d / "APKINDEX.tar.gz").unlink(missing_ok=True)
        (d / "Packages.adb").unlink(missing_ok=True)
        # try removing the stage dir, but keep it if there is still stuff in it
        try:
            d.rmdir()
            d.parent.rmdir()
        except Exception:
            pass
        # finally reindex
        log.out(f"Rebuilding index for {ad}...")
        cli.build_index(ad, epoch)

    return unstage is not None


def clear(arch, force=False):
    with flock.lock(flock.repolock(arch)):
        with flock.lock(flock.stagelock(arch)):
            return _do_clear(arch, force)
