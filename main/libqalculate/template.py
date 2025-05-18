pkgname = "libqalculate"
# match to qalculate-gtk/qt (desynced temporarily for 5.5.2)
pkgver = "5.5.2"
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
    "curl-devel",
    "libxml2-devel",
    "mpfr-devel",
    "readline-devel",
]
pkgdesc = "Multi-purpose desktop calculator library"
license = "GPL-2.0-or-later"
url = "https://qalculate.github.io"
source = f"https://github.com/Qalculate/libqalculate/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3b8f65583779fb584a0e2fa7be95bfcc8a7e71e8e4d2ba64f00856640d32b805"


@subpackage("libqalculate-devel")
def _(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()


@subpackage("libqalculate-progs")
def _(self):
    self.renames = ["qalc"]

    return self.default_progs()
