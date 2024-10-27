pkgname = "libquotient"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DQuotient_INSTALL_TESTS=OFF",
]
# needs running server
make_check_args = ["-E", "(testolmaccount|testcrosssigning|testkeyimport)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "olm-devel",
    "qt6-qtbase-devel",
    "qtkeychain-devel",
]
pkgdesc = "Qt library for Matrix clients"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://quotient-im.github.io/libQuotient"
source = f"https://github.com/quotient-im/libQuotient/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5e607eb978a5daa82e2186cd92f0d964cb820c72cfad95ed2adda4525ed923b5"


def post_install(self):
    # android only
    self.uninstall("usr/share/ndk-modules")


@subpackage("libquotient-devel")
def _(self):
    self.depends += [
        "olm-devel",
        "openssl-devel",
        "qt6-qtbase-devel",
        "qtkeychain-devel",
    ]
    return self.default_devel()
