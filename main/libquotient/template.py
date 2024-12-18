pkgname = "libquotient"
pkgver = "0.9.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://quotient-im.github.io/libQuotient"
source = f"https://github.com/quotient-im/libQuotient/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0a1fd19c9f6e4d93c60fbec5ab4ca84961781e6d00105a4437ecd14aaea36bc9"


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
