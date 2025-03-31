pkgname = "libqalculate"
# match to qalculate-gtk/qt
pkgver = "5.5.1"
pkgrel = 1
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
    "curl-devel",
    "libxml2-devel",
    "mpfr-devel",
    "readline-devel",
]
pkgdesc = "Multi-purpose desktop calculator library"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/libqalculate/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8850a71ceb7a16e8b161edc2f11e2d76bd7c298abe9ddd68f43edf1bdc34aaee"


@subpackage("libqalculate-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libqalculate-progs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("qalc")]

    return self.default_progs()
