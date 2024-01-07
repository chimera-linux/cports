from cbuild.core import chroot, logger
from cbuild.apk import cli

import re


def invoke(pkg):
    if not pkg.options["scanpkgconf"] or pkg.stage == 0:
        return

    pcs = {}
    pcset = {}

    for p in pkg.provides:
        if not p.startswith("pc:"):
            continue
        pcname = p[3:]
        eq = pcname.find("=")
        if eq < 0:
            pkg.error(f"invalid explicit .pc file: {soname}")
        pcname = pcname[:eq]
        sfx = pcname[eq + 1 :]
        pcset[pcname] = True
        logger.get().out_plain(f"   pc: {pcname}={sfx} (explicit)")

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
            "--modversion",
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
            pkg.error("failed scanning .pc files (missing pkgconf?)")
        # sanitize version for apk
        mver = pcc.stdout.decode().strip()
        mver = re.sub("-(alpha|beta|rc|pre)", "_\\1", mver)
        # fallback
        if len(mver) == 0:
            mver = "0"
        elif not cli.check_version(mver):
            # test with apk
            pkg.error(f"invalid pkgconf version {mver}")
        if sn in pcset:
            logger.get().out_plain(f"   pc: {sn}={mver} from {rlp} (skipped)")
        else:
            pcs[sn] = f"{sn}={mver}"
            logger.get().out_plain(f"   pc: {sn}={mver} from {rlp}")

    for f in pkg.destdir.glob("usr/lib/pkgconfig/*.pc"):
        scan_pc(f)

    for f in pkg.destdir.glob("usr/share/pkgconfig/*.pc"):
        scan_pc(f)

    pkg.pc_provides = list(pcs.values())
