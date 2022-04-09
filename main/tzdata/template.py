pkgname = "tzdata"
pkgver = "2022a"
pkgrel = 0
makedepends = ["musl-devel-static", "libunwind-devel-static"]
pkgdesc = "Time zone and daylight-saving time data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.iana.org/time-zones"
source = [
    f"http://www.iana.org/time-zones/repository/releases/tzdata{pkgver}.tar.gz",
    f"https://github.com/eggert/tz/archive/{pkgver}.tar.gz"
]
sha256 = [
    "ef7fffd9f4f50f4f58328b35022a32a5a056b245c5cb3d6791dddb342f871664",
    "e9d82a851a15bb5db2cbaae2c3fc633743ad9edc069e3738c5e8908978064ed8"
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

    with self.profile("host"):
        compiler.C(self).invoke(
            [f"tz-{pkgver}/zic.c"], "zic", flags = ["-static"]
        )

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
