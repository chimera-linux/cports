from cbuild.core import logger, paths, chroot, profile, template
from cbuild.util import flock
from cbuild.apk import cli, util as autil

import json
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

    def _query_apk(*args):
        ret = _call_apk(
            "query", "--format=json", "--all-matches", "--from=none", *args
        )
        if ret.returncode != 0 or len(ret.stdout) == 0:
            return None
        return json.loads(ret.stdout.decode())

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

    # --repository arguments list for query
    brs = []
    # pairs of stage + real repo urls
    srs = []

    # filter repos that have both stage and repo
    for d in rs:
        reld = str(d.relative_to(stagep).parent.parent)
        # only stage exists, so nothing is replacing anything
        ad = rrm.get(reld, None)
        if not ad:
            continue
        srs += [(str(d), str(ad))]
        brs += ["--repository", str(d), "--repository", str(ad)]

    # do a big query for providers
    # this gets us a big array and isn't super useful for further matching
    # so we need to turn it into a more useful lookup structure...
    provq = _query_apk(
        "--fields=name,provides,repositories",
        *brs,
        "*",
    )

    # first build a map of maps, { name => { repo => providers } }
    provm = {}
    for p in provq:
        provs = sorted(p.get("provides", []))
        pkgn = p["name"]
        if pkgn not in provm:
            provm[pkgn] = {}
        for repo in p["repositories"]:
            provm[pkgn][repo] = provs

    # now we have something to go over; go back to staged repos
    for d, ad in srs:
        # go over each package staged in d
        for p, rprovs in provm.items():
            # package not staged here
            if d not in rprovs:
                continue
            # staged providers identical to repo providers; drop
            if ad in rprovs and rprovs[d] == rprovs[ad]:
                continue
            # accumulate stage providers...
            for pr in rprovs[d]:
                vp = pr.find("=")
                if vp > 0:
                    added[pr[0:vp]] = pr[vp + 1 :]
                else:
                    added[pr] = True
            # accumulate repo providers, may be none in the case of there
            # being both repos but only stage having this specific package
            if ad in rprovs:
                for pr in rprovs[ad]:
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

    # do a big query for dependencies of revdeps
    # this once again gets us a big array that's not useful for checks
    depq = _query_apk(
        "--fields=name,depends,repositories",
        *rlist,
        *revdeps.keys(),
    )

    # build a map { name => { repo => depends } }
    # we only care about one repo; the one that is the first in the priority
    # list (rs followed by rr) but we can't filter that until we have them all
    depm = {}
    for p in depq:
        deps = sorted(p.get("depends", []))
        pkgn = p["name"]
        if pkgn not in depm:
            depm[pkgn] = {}
        for repo in p["repositories"]:
            depm[pkgn][repo] = deps

    # filter it now
    for pkgn in list(depm.keys()):
        for r in rs + rr:
            tr = str(r)
            if tr in depm[pkgn]:
                depm[pkgn] = depm[pkgn][tr]
                break

    # for each revdep, do a dep check using potentially staged packages
    # ensure that there is no dependency on a provider that was dropped
    # without a replacement
    for d in revdeps:
        # verify each dep
        for ad in depm[d]:
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
                    ret = autil.version_compare(av, dv)
                    if ret < 0:
                        # constraint ver is lower than provider ver
                        # skip constraints that ask for a smaller/equal version
                        if ao == "=" or ao.startswith("<"):
                            continue
                    elif ret > 0:
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
                    ret = autil.version_compare(av, nv)
                    if ret < 0:
                        # constraint ver is lower than provider ver
                        if ao.startswith(">"):
                            continue
                    elif ret > 0:
                        # constraint ver is larger than provider ver
                        if ao.startswith("<"):
                            continue
                    else:
                        # constraint ver and provider ver are the same
                        if ao != ">":
                            continue
                # satisfied old constraints but not any new ones
                # that means it's a considered dependency
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
