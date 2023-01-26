from cbuild.core import logger, paths, chroot
from cbuild.util import flock
from cbuild.apk import cli

import time
import pathlib
import tempfile
import subprocess

# this one has the dummy root available
def _check_stage(sroot, stlist, arch, signkey):
    added = {}
    dropped = {}
    replaced = {}
    revdeps = {}

    def _call_apk(*args):
        return subprocess.run([
            paths.apk(), "--quiet", "--arch", arch, "--allow-untrusted",
            "--root", sroot, *args
        ], capture_output = True)

    # full repo list for revdep search
    rlist = []

    repop = paths.repository()
    stagep = paths.stage_repository()
    rr = [] # regular repos
    rs = [] # stage repos
    for f in repop.rglob("APKINDEX.tar.gz"):
        p = f.parent
        if p.name != arch:
            continue
        rr.append(p.parent)
    for f in stagep.rglob("APKINDEX.tar.gz"):
        p = f.parent
        if p.name != arch:
            continue
        rs.append(p.parent)
    rr.sort()
    rs.sort()
    for r in rs:
        rlist += ["--repository", str(r)]
    # regular repos are last in the list
    for r in rr:
        rlist += ["--repository", str(r)]

    for d, ad in stlist:
        # only stage exists, so nothing is replacing anything
        if not (ad / "APKINDEX.tar.gz").is_file():
            continue
        # search for all staged packages
        ret = _call_apk("--repository", str(d.parent), "search")
        # go over each staged package
        for p in ret.stdout.strip().decode().split():
            # get providers of both
            pr = _call_apk(
                "--repository", str(d.parent), "--repository", str(ad.parent),
                "info", "--provides", p
            )
            prout = pr.stdout.decode().split("\n\n")
            if len(prout) < 3:
                # TODO: handle this?
                continue
            # stage providers
            stpr = set(prout[0].strip().split())
            # repo providers
            rppr = set(prout[1].strip().split())
            # if they are the same, just skip
            if stpr == rppr:
                continue
            # accumulate stage providers
            for pr in stpr:
                vp = pr.find("=")
                if vp > 0:
                    added[pr[0:vp]] = pr[vp + 1:]
                else:
                    added[pr] = True
            # accumulate repo providers
            for pr in rppr:
                vp = pr.find("=")
                if vp > 0:
                    dropped[pr[0:vp]] = pr[vp + 1:]
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
    for d in dropped:
        ret = _call_apk(*rlist, "search", "--exact", "--all", "--rdepends", d)
        for pn in ret.stdout.strip().decode().split():
            revdeps[pn] = True

    # potentially missing deps
    checkdeps = {}

    # for each revdep, do a dep check using potentially staged packages
    # ensure that there is no dependency on a provider that was dropped
    # without a replacement
    for d in revdeps:
        ret = _call_apk(*rlist, "info", "--depends", d)
        sout = ret.stdout
        # highest priority boundary
        bdr = sout.find(b"\n\n")
        if bdr < 0:
            continue
        # dependencies of the most significant (maybe staged) provider
        deps = sout[0:bdr].strip().decode().split()
        # verify each dep
        for ad in deps:
            av = None
            ao = None
            # check if versioned
            for i, c in enumerate(ad):
                # get the version and operator
                if c == "=":
                    av = ad[i + 1:]
                    ao = c
                    ad = ad[0:i]
                    break
                elif c == "<" or c == ">":
                    if ad[i + 1:i + 2] == "=":
                        av = ad[i + 2:]
                        ao = c + "="
                    else:
                        av = ad[i + 1:]
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

    # if there were such cases, further narrow thme down to ensure that
    # we are not dealing with something that still has another suitable
    # provider, as that should not stage us
    for d in list(checkdeps.keys()):
        ret = _call_apk(*rlist, "search", "--all", "--exact", d)
        # for each provider of sketchy dependency, if it's provided
        # using a name that was not deleted, it's probably okay
        for pd in ret.stdout.strip().decode().split():
            if pd not in replaced:
                del checkdeps[d]
                break

    # we can safely unstage as there is ntohing left
    if len(checkdeps) == 0:
        return True

    logger.get().out("Cannot unstage repositories:")

    # ensure repo remains staged
    # also print a list of stuff to rebuild and what causes
    # it to require rebuilding for informational purposes
    for d in checkdeps:
        print(f" rebuild: {', '.join(checkdeps[d])} ({d})")

    return False

def check_stage(stagelist, arch, signkey):
    # we need a dummy root; since we use apk info to query providers,
    # and there is no way to prevent that from including installed
    # stuff in the output, this is the only good way
    with tempfile.TemporaryDirectory() as stageroot:
        stageroot = pathlib.Path(stageroot)
        chroot.initdb(stageroot)
        return _check_stage(stageroot, stagelist, arch, signkey)

def _do_clear(arch, signkey, force):
    repop = paths.repository()
    sroot = paths.stage_repository()
    log = logger.get()

    log.out(f"Clearing staged {arch} repos for {repop}...")

    # a list of all stage repos that we have
    stagelist = []

    # fetch all pairs of stage repos + actual repos
    for ri in sroot.rglob("APKINDEX.tar.gz"):
        ri = ri.parent
        if ri.name != arch:
            continue
        stagelist.append((ri, repop / ri.relative_to(sroot)))

    if not force and not check_stage(stagelist, arch, signkey):
        return

    # FIXME: compute from git if possible
    epoch = int(time.time())

    for d, ad in stagelist:
        try:
            ad.rmdir()
        except:
            pass
        # just migrate if possible, easier this way
        if not ad.is_dir():
            log.out(f"Migrating stage from {d} to {ad}...")
            d.rename(ad)
            continue
        # else merge the directories
        log.out(f"Merging stage from {d} to {ad}...")
        for f in d.glob("*.apk"):
            f.rename(ad / f.name)
        # clear the stage index, we won't need it
        (d / "APKINDEX.tar.gz").unlink()
        # try removing the stage dir, but keep it if there is still stuff in it
        try:
            d.rmdir()
            d.parent.rmdir()
        except:
            pass
        # finally reindex
        log.out(f"Rebuilding index for {ad}...")
        cli.build_index(ad, epoch, signkey)

def clear(arch, signkey, force = False):
    with flock.lock(flock.repolock(arch)):
        _do_clear(arch, signkey, force)
