pkgname = "tzdata"
pkgver = "2024a"
pkgrel = 0
hostmakedepends = [
    "musl-devel-static",
    "libunwind-devel-static",
    "libatomic-chimera-devel-static",
]
pkgdesc = "Time zone and daylight-saving time data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.iana.org/time-zones"
source = [
    f"http://www.iana.org/time-zones/repository/releases/tzdata{pkgver}.tar.gz",
    f"https://github.com/eggert/tz/archive/{pkgver}.tar.gz",
]
sha256 = [
    "0d0434459acbd2059a7a8da1f3304a84a86591f6ed69c6248fffa502b6edffe3",
    "1f562444eb9a646ac9eb4cf7ed9a149e00f7834e373032dd0b2cc773341924a8",
]
# no tests
options = ["bootstrap", "!check", "hardlinks", "!scantrigdeps"]

if self.stage == 0:
    makedepends = list(hostmakedepends)


def do_build(self):
    from cbuild.util import compiler

    with open(self.cwd / f"tz-{pkgver}/version.h", "w") as vh:
        vh.write(
            """
static char const PKGVERSION[]="unknown";
static char const TZVERSION[]="unknown";
static char const REPORT_BUGS_TO[]="none";
"""
        )

    with open(self.cwd / f"tz-{pkgver}/tzdir.h", "w") as vh:
        vh.write(
            """
#ifndef TZDEFAULT
#define TZDEFAULT "UTC"
#endif
#ifndef TZDIR
#define TZDIR "/usr/share/zoneinfo"
#endif
"""
        )

    with self.profile("host"):
        compiler.C(self).invoke(
            [f"tz-{pkgver}/zic.c"], "zic", flags=["-static"]
        )


def do_install(self):
    tzs = [
        "africa",
        "antarctica",
        "asia",
        "australasia",
        "europe",
        "northamerica",
        "southamerica",
        "etcetera",
        "backward",
        "factory",
    ]

    self.do(
        self.chroot_cwd / "zic",
        "-b",
        "fat",
        "-d",
        self.chroot_destdir / "usr/share/zoneinfo",
        *tzs,
    )

    self.do(
        self.chroot_cwd / "zic",
        "-b",
        "fat",
        "-d",
        self.chroot_destdir / "usr/share/zoneinfo/posix",
        *tzs,
    )

    self.do(
        self.chroot_cwd / "zic",
        "-b",
        "fat",
        "-d",
        self.chroot_destdir / "usr/share/zoneinfo/right",
        "-p",
        "America/New_York",
        *tzs,
    )

    for f in ["iso3166", "zone1970", "zone"]:
        self.install_file(f"{f}.tab", "usr/share/zoneinfo", mode=0o444)

    self.install_file("leap-seconds.list", "usr/share/zoneinfo")
    self.install_file(self.files_path / "tzdata.conf", "usr/lib/tmpfiles.d")
