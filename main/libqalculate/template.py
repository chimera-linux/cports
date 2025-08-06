pkgname = "libqalculate"
# match to qalculate-gtk/qt
pkgver = "5.7.0"
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
    "curl-devel",
    "gmp-devel",
    "icu-devel",
    "libxml2-devel",
    "mpfr-devel",
    "readline-devel",
]
pkgdesc = "Multi-purpose desktop calculator library"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/libqalculate/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "050c9005cc05395a93d70547bf5ae44b652bf527c01f153b2d29191ab84bb74c"


@subpackage("libqalculate-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libqalculate-progs")
def _(self):
    self.renames = ["qalc"]

    return self.default_progs()
