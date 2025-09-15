from cbuild.core import chroot, logger
from cbuild.apk import cli

import re
import pathlib


def _match_skipprov(pkg, f, norel=False):
    if norel:
        rf = f
    else:
        rf = f.relative_to(pkg.destdir)
    for mf in pkg.skip_providers:
        if rf.match(mf):
            return None
    return rf


def _invoke_cmd(pkg):
    if not pkg.options["scancmd"] or pkg.autopkg:
        return

    cmds = []
    cmdset = {}

    for p in pkg.provides:
        if not p.startswith("cmd:"):
            continue
        cmdname = p[4:]
        versep = cmdname.find("=")
        if versep > 0:
            cmdset[cmdname[:versep]] = True
        else:
            cmdset[cmdname] = True
        logger.get().out_plain(
            f"  \f[cyan]cmd: \f[orange]{cmdname}\f[] \f[green](explicit)\f[]"
        )

    for f in pkg.destdir.glob("usr/bin/*"):
        if f.name in cmdset:
            continue
        if not _match_skipprov(pkg, f):
            continue
        # forbidden characters
        if any(v in f.name for v in "[]=<>~"):
            continue
        logger.get().out_plain(
            f"  \f[cyan]cmd: \f[orange]{f.name}\f[] from \f[green]usr/bin\f[]"
        )
        if pkg.alternative:
            cmds.append(f.name + "=0")
        else:
            cmds.append(f.name + f"={pkg.pkgver}-r{pkg.pkgrel}")

    cmds.sort()

    if len(cmds) == 0:
        return

    pkg.cmd_provides = cmds


def _invoke_pc(pkg):
    if not pkg.options["scanpkgconf"] or pkg.stage == 0 or pkg.autopkg:
        return

    pcs = {}
    pcset = {}

    for p in pkg.provides:
        if not p.startswith("pc:"):
            continue
        pcname = p[3:]
        eq = pcname.find("=")
        if eq < 0:
            pkg.error(f"invalid explicit .pc file: {pcname}")
        pcname = pcname[:eq]
        sfx = pcname[eq + 1 :]
        pcset[pcname] = True
        logger.get().out_plain(
            f"  \f[cyan]pc: \f[orange]{pcname}={sfx}\f[] \f[green](explicit)\f[]"
        )

    def scan_pc(v):
        if not v.exists():
            return
        if not _match_skipprov(pkg, f):
            return
        fn = v.name
        sn = v.stem
        # maybe provided in two locations
        if sn in pcs:
            pkg.error(f"multiple paths provide one .pc: {fn}")
        # we will be scanning in-chroot
        rlp = v.relative_to(pkg.destdir).parent
        cdv = pkg.chroot_destdir / rlp
        pcc = chroot.enter(
            "pkg-config",
            "--print-provides",
            sn,
            capture_output=True,
            bootstrapping=False,
            ro_root=True,
            ro_build=True,
            unshare_all=True,
            env={
                "PKG_CONFIG_PATH": str(cdv),
                "PKG_CONFIG_MAXIMUM_TRAVERSE_DEPTH": "1",
            },
        )
        if pcc.returncode != 0:
            pkg.error(
                "failed scanning .pc files",
                hint="maybe 'pkgconf' is missing from 'hostmakedepends'",
            )
        # parse the output
        for ln in pcc.stdout.strip().splitlines():
            plist = ln.decode().split(" = ")
            if len(plist) != 2:
                pkg.error(
                    f"failed scanning .pc files (invalid provider '{ln}' in '{sn}')"
                )
            pname, mver = plist
            # sanitize version for apk
            mver = re.sub(r"-(alpha|beta|rc|pre)", "_\\1", mver)
            # fallback
            if len(mver) == 0 or pkg.alternative:
                mver = "0"
            elif not cli.check_version(mver):
                # test with apk
                pkg.error(
                    f"invalid pkgconf version {mver}",
                    hint="the version in the .pc file must be compatible with apk format",
                )
            if pname in pcset:
                logger.get().out_plain(
                    f"  \f[cyan]pc: \f[orange]{pname}={mver}\f[] from \f[green]{rlp} \f[purple](skipped)\f[]"
                )
            else:
                pcs[pname] = f"{pname}={mver}"
                logger.get().out_plain(
                    f"  \f[cyan]pc: \f[orange]{pname}={mver}\f[] from \f[green]{rlp}\f[]"
                )

    for f in pkg.destdir.glob("usr/lib/pkgconfig/*.pc"):
        scan_pc(f)

    for f in pkg.destdir.glob("usr/share/pkgconfig/*.pc"):
        scan_pc(f)

    pkg.pc_provides = list(pcs.values())


def _matches_lib(soname, root):
    # no soname: drop from earch
    if not soname:
        return False

    # versioned or unversioned soname
    if re.match(r"^\w+(.*)+\.so(\.\d+)*$", soname):
        # versioned soname: match anywhere
        if re.search(r"\d+$", soname):
            return True

        # unversioned soname: only if in libdir
        return str(root) == "usr/lib"


def _invoke_so(pkg):
    if not pkg.options["scanshlibs"] or pkg.autopkg:
        return

    asonames = []
    curelf = pkg.rparent.current_elfs

    soset = {}

    # add explicit provides
    for p in pkg.provides:
        if not p.startswith("so:"):
            continue
        soname = p[3:]
        eq = soname.find("=")
        if eq < 0:
            pkg.error(f"invalid explicit shlib: {soname}")
        sfx = soname[eq + 1 :]
        soname = soname[:eq]
        soset[soname] = True
        logger.get().out_plain(
            f"  \f[cyan]SONAME: \f[orange]{soname}={sfx} \f[green](explicit)\f[]"
        )

    for fp, finfo in curelf.items():
        fp = pathlib.Path(fp)

        soname, needed, pname, static, etype, interp, foreign = finfo

        # we only care about our own
        if pname != pkg.pkgname:
            continue

        if not _match_skipprov(pkg, fp, True):
            continue

        # foreign-machine elfs are not scanned
        if foreign:
            continue

        sfxs = fp.suffixes

        # we don't care about anything before the .so
        while len(sfxs) > 0 and sfxs[0] != ".so":
            sfxs = sfxs[1:]

        if _matches_lib(soname, fp.parent):
            autosfx = "".join(sfxs[1:])[1:]
            if len(autosfx) == 0:
                autosfx = "0"
            elif not cli.check_version(autosfx):
                pkg.error(f"invalid so version {autosfx}")

            if soname not in soset:
                asonames.append(
                    (soname, autosfx if not pkg.alternative else "0")
                )
                logger.get().out_plain(
                    f"  \f[cyan]SONAME: \f[orange]{soname}\f[] from \f[green]{fp.parent}\f[]"
                )
            else:
                logger.get().out_plain(
                    f"  \f[cyan]SONAME: \f[orange]{soname}\f[] from \f[green]{fp.parent} \f[orange](skipped)\f[]"
                )

    pkg.aso_provides = asonames


def _invoke_svc(pkg):
    if not pkg.options["scanservices"] or (
        pkg.autopkg and not pkg.pkgname.endswith("-dinit")
    ):
        return

    svcs = []
    svcset = {}

    for p in pkg.provides:
        if p.startswith("svc:"):
            svcpfx = p[0:4]
            svcname = p[4:]
        elif p.startswith("usvc:"):
            svcpfx = p[0:5]
            svcname = p[5:]
        else:
            continue
        versep = svcname.find("=")
        if versep > 0:
            svcset[svcname[:versep]] = True
        else:
            svcset[svcname] = True
        logger.get().out_plain(
            f"  \f[cyan]{svcpfx} \f[orange]{svcname}\f[] \f[green](explicit)\f[]"
        )

    def _scan_svc(f, pfx):
        # only consider files...
        if not f.is_file():
            return
        if not _match_skipprov(pkg, f):
            return
        # explicitly provided
        if f"{pfx}:{f.name}" in svcset:
            return
        # forbidden characters
        if any(v in f.name for v in "[]=<>~"):
            return
        logger.get().out_plain(
            f"  \f[cyan]{pfx}: \f[orange]{f.name}\f[] from \f[green]{f.parent.relative_to(pkg.destdir)}\f[]"
        )
        if pkg.alternative:
            svcs.append(pfx + ":" + f.name + "=0")
        else:
            svcs.append(pfx + ":" + f.name + f"={pkg.pkgver}-r{pkg.pkgrel}")

    for f in pkg.destdir.glob("usr/lib/dinit.d/*"):
        # for dinit-chimera we only care about providing targets
        if pkg.rparent.pkgname == "dinit-chimera" and not f.name.endswith(
            ".target"
        ):
            continue
        _scan_svc(f, "svc")

    for f in pkg.destdir.glob("usr/lib/dinit.d/user/*"):
        _scan_svc(f, "usvc")

    svcs.sort()

    if len(svcs) == 0:
        return

    pkg.svc_provides = svcs


def invoke(pkg):
    _invoke_cmd(pkg)
    _invoke_pc(pkg)
    _invoke_so(pkg)
    _invoke_svc(pkg)
