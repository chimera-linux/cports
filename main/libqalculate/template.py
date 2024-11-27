pkgname = "libqalculate"
# match to qalculate-gtk/qt
pkgver = "5.4.0.1"
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
sha256 = "195c4f23495fae9429b313ac6a9e9ae089a0f1fb8fb0bc72959ba0fddf6e0b28"


@subpackage("libqalculate-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("qalc")
def _(self):
    self.pkgdesc = "Command-line calculator"
    return ["usr/bin/qalc", "usr/share/man/man1/qalc.1"]
