pkgname = "libquotient"
pkgver = "0.9.6.1"
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
    "qt6-qtbase-private-devel",  # qjson_p.h
    "qtkeychain-devel",
]
pkgdesc = "Qt library for Matrix clients"
license = "LGPL-2.1-or-later"
url = "https://quotient-im.github.io/libQuotient"
source = f"https://github.com/quotient-im/libQuotient/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ac0fe5df480fa893d3e16da626bf5028c944e9b41f504f6fe0fe49273247d636"


def post_install(self):
    # android only
    self.uninstall("usr/share/ndk-modules")


@subpackage("libquotient-devel")
def _(self):
    self.depends += [
        "olm-devel",
        "openssl3-devel",
        "qt6-qtbase-devel",
        "qtkeychain-devel",
    ]
    return self.default_devel()
