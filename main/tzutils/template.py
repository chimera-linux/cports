pkgname = "tzutils"
pkgver = "2024b"
pkgrel = 0
build_style = "makefile"
make_build_args = ["KSHELL=/bin/sh"]
make_install_args = ["ZICDIR=/usr/bin", "ZFLAGS=-b fat"]
hostmakedepends = []
checkdepends = ["curl", "perl"]
pkgdesc = "Time zone and daylight-saving time utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://www.iana.org/time-zones"
source = f"{url}/repository/releases/tzdb-{pkgver}.tar.lz"
sha256 = "22674a67786d3ec1b0547305904011cb2b9126166e72abbbea39425de5595233"
hardening = ["vis", "cfi"]
# needs network access
options = ["!check"]


if self.profile().cross:
    hostmakedepends += ["tzutils"]
    make_install_args += ["zic=/usr/bin/zic"]


def post_install(self):
    # localtime
    self.uninstall("etc")
    # useless static lib
    self.uninstall("usr/lib")
    # irrelevant c manpages
    self.uninstall("usr/share/man/man3")
    # don't care
    self.uninstall("usr/share/zoneinfo-posix")
    # this will be split
    self.rename("usr/share/zoneinfo-leaps", "zoneinfo/right")
    # tmpfiles
    self.install_tmpfiles(self.files_path / "tzdata.conf", name="tzdata")
    # used by some software, e.g. hare's standard library
    self.install_file("leap-seconds.list", "usr/share/zoneinfo")


@subpackage("tzdata-right")
def _(self):
    self.pkgdesc = "Time zone and daylight-saving time data"
    self.subdesc = "TAI"
    self.options = ["hardlinks"]
    self.depends = [self.with_pkgver("tzdata")]

    return ["usr/share/zoneinfo/right"]


@subpackage("tzdata")
def _(self):
    self.pkgdesc = "Time zone and daylight-saving time data"
    # cannot be symlinks; some software does not like it
    self.options = ["hardlinks"]

    return ["usr/lib/tmpfiles.d", "usr/share/zoneinfo"]
