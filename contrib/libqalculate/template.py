pkgname = "libqalculate"
# match to qalculate-gtk/qt
pkgver = "5.1.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gmp-devel",
    "icu-devel",
    "libcurl-devel",
    "libxml2-devel",
    "mpfr-devel",
    "readline-devel",
]
pkgdesc = "Multi-purpose desktop calculator library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/libqalculate/releases/download/v{pkgver}/libqalculate-{pkgver}.tar.gz"
sha256 = "04db2d1c8dc0d5a006971bb138aa71d4a944275dde8dbf952ad8b59bf499aba1"


@subpackage("libqalculate-devel")
def _devel(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("qalc")
def _qalc(self):
    self.pkgdesc = "Command-line calculator"
    return ["usr/bin/qalc", "usr/share/man/man1/qalc.1"]
