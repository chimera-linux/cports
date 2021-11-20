pkgname = "tzdata"
pkgver = "2021e"
pkgrel = 0
pkgdesc = "Time zone and daylight-saving time data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.iana.org/time-zones"
source = [
    f"http://www.iana.org/time-zones/repository/releases/tzdata{pkgver}.tar.gz",
    f"https://github.com/eggert/tz/archive/{pkgver}.tar.gz"
]
sha256 = [
    "07ec42b737d0d3c6be9c337f8abb5f00554a0f9cc4fcf01a703d69403b6bb2b1",
    "11908a7f18530ca3013c8458d902a54cdd3382276bdd56891db074b1af4a26b8"
]
# no tests
options = ["bootstrap", "!check", "hardlinks"]

def do_build(self):
    from cbuild.util import compiler

    with open(self.cwd / f"tz-{pkgver}/version.h", "w") as vh:
        vh.write("""
static char const PKGVERSION[]="unknown";
static char const TZVERSION[]="unknown";
static char const REPORT_BUGS_TO[]="none";
""")

    compiler.C(self).invoke([f"tz-{pkgver}/zic.c"], "zic", flags = ["-static"])

def do_install(self):
    tzs = [
        "africa", "antarctica", "asia", "australasia", "europe",
        "northamerica", "southamerica", "etcetera", "backward", "factory"
    ]

    self.do(
        self.chroot_cwd / "zic", "-b", "fat", "-d",
        self.chroot_destdir / "usr/share/zoneinfo", *tzs
    )

    self.do(
        self.chroot_cwd / "zic", "-b", "fat", "-d",
        self.chroot_destdir / "usr/share/zoneinfo/posix", *tzs
    )

    self.do(
        self.chroot_cwd / "zic", "-b", "fat", "-d",
        self.chroot_destdir / "usr/share/zoneinfo/right",
        "-p", "America/New_York", *tzs
    )

    for f in ["iso3166", "zone1970", "zone"]:
        self.install_file(f"{f}.tab", "usr/share/zoneinfo", mode = 0o444)
