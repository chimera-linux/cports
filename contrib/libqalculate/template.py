pkgname = "libqalculate"
# match to qalculate-gtk/qt
pkgver = "5.2.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
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
source = f"https://github.com/Qalculate/libqalculate/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "df48e3693a034afa239f37b445a48b60c07d336073af8e8df8a36e1c6657d37f"


@subpackage("libqalculate-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("qalc")
def _(self):
    self.pkgdesc = "Command-line calculator"
    return ["usr/bin/qalc", "usr/share/man/man1/qalc.1"]
