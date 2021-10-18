pkgname = "tzdata"
pkgver = "2021d"
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
    "d7c188a2b33d4a3c25ee4a9fdc68c1ff462bfdb302cf41343d84ca5942dbddf6",
    "2e6b14cfe3ee389f67887c36436cc40ff11266e5c2213295c1528f42a65dc98e"
]
# no tests
options = ["bootstrap", "!check"]

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

    self.do(self.chroot_cwd / "zic", [
        "-b", "fat", "-d", self.chroot_destdir / "usr/share/zoneinfo"
    ] + tzs)

    self.do(self.chroot_cwd / "zic", [
        "-b", "fat", "-d", self.chroot_destdir / "usr/share/zoneinfo/posix"
    ] + tzs)

    self.do(self.chroot_cwd / "zic", [
        "-b", "fat", "-d", self.chroot_destdir / "usr/share/zoneinfo/right",
        "-p", "America/New_York"
    ] + tzs)

    for f in ["iso3166", "zone1970", "zone"]:
        self.install_file(f"{f}.tab", "usr/share/zoneinfo", mode = 0o444)
