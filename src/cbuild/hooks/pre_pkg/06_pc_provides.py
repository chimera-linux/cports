from cbuild.core import chroot
from cbuild.apk import cli

import re

def invoke(pkg):
    if not pkg.options["scanpkgconf"] or pkg.bootstrapping:
        return

    pcs = {}

    def scan_pc(v):
        fn = v.name
        sn = v.stem
        # maybe provided in two locations
        if sn in pcs:
            pkg.error(f"multiple paths provide one .pc: {fn}")
        # we will be scanning in-chroot
        cdv = pkg.chroot_destdir / v.relative_to(pkg.destdir)
        pcc = chroot.enter(
            "pkg-config", ["--modversion", sn], capture_out = True,
            env = {
                "PKG_CONFIG_PATH": str(cdv.parent),
                "PKG_CONFIG_MAXIMUM_TRAVERSE_DEPTH": "1",
            }
        )
        if pcc.returncode != 0:
            pkg.error("failed scanning .pc files (missing pkgconf?)")
        # sanitize version for apk
        mver = pcc.stdout.decode().strip()
        mver = re.sub("-(alpha|beta|rc|pre)", "_\\1", mver)
        # test with apk
        if not cli.check_version(mver):
            pkg.error(f"invalid pkgconf version {mver}")
        # fallback
        if len(mver) == 0:
            mver = "0"
        pcs[sn] = f"{sn}={mver}"

    for f in pkg.destdir.glob("usr/lib/pkgconfig/*.pc"):
        scan_pc(f)

    for f in pkg.destdir.glob("usr/share/pkgconfig/*.pc"):
        scan_pc(f)

    pcvals = list(pcs.values())
    pcvals.sort()

    if len(pcvals) == 0:
        return

    pkg.pc_provides = pcvals
