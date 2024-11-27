pkgname = "qtkeychain"
pkgver = "0.14.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libsecret-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt library for storing data in the system keychain"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/frankosterfeld/qtkeychain"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a22c708f351431d8736a0ac5c562414f2b7bb919a6292cbca1ff7ac0849cb0a7"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("qtkeychain-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
