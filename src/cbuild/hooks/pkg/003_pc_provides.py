from cbuild.core import chroot, logger
from cbuild.apk import cli

import re


def invoke(pkg):
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
