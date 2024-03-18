pkgname = "tzutils"
pkgver = "2024a"
pkgrel = 3
build_style = "makefile"
make_build_args = ["KSHELL=/bin/sh"]
make_install_args = ["ZICDIR=/usr/bin", "ZFLAGS=-b fat"]
hostmakedepends = []
checkdepends = ["curl", "perl"]
pkgdesc = "Time zone and daylight-saving time utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.iana.org/time-zones"
source = (
    f"https://www.iana.org/time-zones/repository/releases/tzdb-{pkgver}.tar.lz"
)
sha256 = "511af6b467f40b1ec9ac3684d1701793af470f3e29ddfb97b82be438e8601a7a"
hardening = ["vis", "cfi"]
# needs network access
options = ["!check"]


if self.profile().cross:
    hostmakedepends += ["tzutils"]
    make_install_args += ["zic=/usr/bin/zic"]


def post_install(self):
    # localtime
    self.rm(self.destdir / "etc", recursive=True)
    # useless static lib
    self.rm(self.destdir / "usr/lib", recursive=True)
    # irrelevant c manpages
    self.rm(self.destdir / "usr/share/man/man3", recursive=True)
    # don't care
    self.rm(self.destdir / "usr/share/zoneinfo-posix")
    # this will be split
    self.mv(
        self.destdir / "usr/share/zoneinfo-leaps",
        self.destdir / "usr/share/zoneinfo/right",
    )
    # tmpfiles
    self.install_file(self.files_path / "tzdata.conf", "usr/lib/tmpfiles.d")


@subpackage("tzdata-right")
def _tzdatar(self):
    self.pkgdesc = "Time zone and daylight-saving time data (TAI)"
    self.options = ["hardlinks"]
    self.depends = [f"tzdata={pkgver}-r{pkgrel}"]

    return ["usr/share/zoneinfo/right"]


@subpackage("tzdata")
def _tzdata(self):
    self.pkgdesc = "Time zone and daylight-saving time data"
    # cannot be symlinks; some software does not like it
    self.options = ["hardlinks"]

    return ["usr/lib/tmpfiles.d", "usr/share/zoneinfo"]
