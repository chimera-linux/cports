pkgname = "tzdata"
pkgver = "2023d"
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
    "dbca21970b0a8b8c0ceceec1d7b91fa903be0f6eca5ae732b5329672232a08f3",
    "487df6ff5f4a577fd96568d0fd0a22e8062b0ec59af7ad3e66b5dd23a85cfc1c",
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
