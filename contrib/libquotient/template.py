pkgname = "libquotient"
pkgver = "0.8.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_WITH_QT6=ON",
    "-DQuotient_ENABLE_E2EE=ON",
    "-DQuotient_INSTALL_TESTS=OFF",
]
# needs running server
make_check_args = ["-E", "testolmaccount"]
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
sha256 = "12ff2fa8b80a934b9dd88fa3416a4b88e94bc0e18a8df0dcebfc90614dd2f5c9"


def post_install(self):
    # android only
    self.uninstall("usr/share/ndk-modules")


@subpackage("libquotient-devel")
def _devel(self):
    self.depends += [
        "olm-devel",
        "openssl-devel",
        "qt6-qtbase-devel",
        "qtkeychain-devel",
    ]
    return self.default_devel()
