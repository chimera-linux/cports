pkgname = "tzdb"
pkgver = "2026c"
pkgrel = 0
build_style = "makefile"
make_build_args = ["KSHELL=/bin/sh"]
make_install_args = ["ZICDIR=/usr/bin", "ZFLAGS=-b fat", "REDO=posix_right"]
hostmakedepends = []
checkdepends = ["curl", "perl"]
provides = [self.with_pkgver("tzdata")]
pkgdesc = "Time zone database"
license = "custom:none"
url = "https://www.iana.org/time-zones"
source = f"{url}/repository/releases/tzdb-{pkgver}.tar.lz"
sha256 = "427a11b1c5f2ebccad18f11650221c4f0465b4f1bb7f44dd02ff192d2808d944"
hardening = ["vis", "cfi"]
# needs network access
# cannot be symlinks; some software does not like it
options = ["!check", "hardlinks"]


if self.profile().cross:
    hostmakedepends += ["tzdb-progs"]
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


@subpackage("tzdb-right")
def _(self):
    self.subdesc = "TAI"
    self.options = ["hardlinks"]
    self.depends = [self.parent]
    self.provides = [self.with_pkgver("tzdata-right")]

    return ["usr/share/zoneinfo/right"]


@subpackage("tzdb-progs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("tzutils")]

    return self.default_progs()
