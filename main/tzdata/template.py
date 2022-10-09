pkgname = "tzdata"
pkgver = "2022d"
pkgrel = 0
hostmakedepends = ["musl-devel-static", "libunwind-devel-static"]
pkgdesc = "Time zone and daylight-saving time data"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.iana.org/time-zones"
source = [
    f"http://www.iana.org/time-zones/repository/releases/tzdata{pkgver}.tar.gz",
    f"https://github.com/eggert/tz/archive/{pkgver}.tar.gz"
]
sha256 = [
    "6ecdbee27fa43dcfa49f3d4fd8bb1dfef54c90da1abcd82c9abcf2dc4f321de0",
    "797ebde2d30259f8c008fffb5916e58c7f885db856d96c8abfe9e99404422ecb"
]
# no tests
options = ["bootstrap", "!check", "hardlinks"]

if self.stage == 0:
    makedepends = list(hostmakedepends)

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
