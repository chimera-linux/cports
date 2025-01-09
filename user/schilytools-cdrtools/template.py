# a "maintained" fork of the old tree at https://sourceforge.net/projects/schilytools ,
# to provide cdrtools (https://sourceforge.net/projects/cdrtools)
# this stuff is really scuffed but this modern-maintained version is the easiest to build
pkgname = "schilytools-cdrtools"
pkgver = "2024.03.21"
pkgrel = 0
build_style = "makefile"
make_build_args = ["INS_BASE=/usr"]
make_install_args = ["-j1", "CHGRPPROG=true", *make_build_args]
make_use_env = True
hostmakedepends = ["libcap-progs"]
makedepends = ["e2fsprogs-devel", "linux-headers"]
# provide the default distro-name-expected name, since in most places it's unprefixed
provides = [self.with_pkgver("cdrtools")]
pkgdesc = "Collection of tools formerly made by Jörg Schilling"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
# lol
license = "LGPL-2.1-only AND GPL-2.0-or-later AND custom:CDDL-schily"
url = "https://codeberg.org/schilytools/schilytools"
source = f"{url}/archive/{pkgver.replace('.', '-')}.tar.gz"
sha256 = "4d66bf35a5bc2927248fac82266b56514fde07c1acda66f25b9c42ccff560a02"
# int/aliasing/lto disabled because inheriting an ancient 30 year old C codebase
# and it's most likely broken
# also for most files they're ignored
tool_flags = {"CFLAGS": ["-fno-strict-aliasing"]}
file_modes = {
    "usr/bin/cdrecord": ("root", "root", 0o755),
    "usr/bin/cdda2wav": ("root", "root", 0o755),
    "usr/bin/readcd": ("root", "root", 0o755),
    # drop suid
    "usr/bin/rscsi": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/cdrecord": {
        "security.capability": "cap_sys_resource,cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_ipc_lock,cap_sys_rawio+ep",
    },
    "usr/bin/cdda2wav": {
        "security.capability": "cap_dac_override,cap_sys_admin,cap_sys_nice,cap_net_bind_service,cap_sys_rawio+ep",
    },
    "usr/bin/readcd": {
        "security.capability": "cap_dac_override,cap_sys_admin,cap_net_bind_service,cap_sys_rawio+ep",
    },
}
hardening = ["!int"]
# no tests
options = ["!check", "!lto"]

# todo: make build system suck less ass, respect flags, ..


def post_install(self):
    # epic nice
    # a symlink doesn't work as the install does mkdir on sbindir
    self.mv(">/usr/sbin/*", ">/usr/bin/", glob=True)
    self.uninstall("usr/sbin")

    # cleanup garbage
    # this package has a ton of random junk, but we only have this for cdrtools
    # so, keep only the cdrtools to have them standalone, and nuke the rest
    # yes, it sucks..
    keep = [
        "usr/bin/btcflash",
        "usr/bin/cdda2mp3",
        "usr/bin/cdda2ogg",
        "usr/bin/cdda2wav",
        "usr/bin/cdrecord",
        "usr/bin/devdump",
        "usr/bin/isodebug",
        "usr/bin/isodump",
        "usr/bin/isoinfo",
        "usr/bin/isovfy",
        "usr/bin/mkhybrid",
        "usr/bin/mkisofs",
        "usr/bin/readcd",
        "usr/bin/rscsi",
        "usr/bin/scgcheck",
        "usr/bin/scgskeleton",
        "usr/share/man/man1/btcflash.1.gz",
        "usr/share/man/man1/cdda2mp3.1.gz",
        "usr/share/man/man1/cdda2ogg.1.gz",
        "usr/share/man/man1/cdda2wav.1.gz",
        "usr/share/man/man1/cdrecord.1.gz",
        "usr/share/man/man1/readcd.1.gz",
        "usr/share/man/man1/rscsi.1.gz",
        "usr/share/man/man1/scgcheck.1.gz",
        "usr/share/man/man1/scgskeleton.1.gz",
        "usr/share/man/man8/devdump.8.gz",
        "usr/share/man/man8/isodebug.8.gz",
        "usr/share/man/man8/isodump.8.gz",
        "usr/share/man/man8/isoinfo.8.gz",
        "usr/share/man/man8/isovfy.8.gz",
        "usr/share/man/man8/mkhybrid.8.gz",
        "usr/share/man/man8/mkisofs.8.gz",
        "etc/default/cdrecord",
        "etc/default/rscsi",
        "usr/share/lib/siconv",
        "usr/share/doc/cdda2wav",
        "usr/share/doc/cdrecord",
        "usr/share/doc/mkisofs",
        "usr/share/doc/rscsi",
    ]
    for f in self.destdir.rglob("*"):
        if f.is_dir():
            continue
        path = f.relative_to(self.destdir)
        if str(path) not in keep:
            f.unlink()

    self.install_license("CDDL.Schily.txt")
    self.install_file(
        "^/modules-load.conf", "usr/lib/modules-load.d", name="cdrecord.conf"
    )
