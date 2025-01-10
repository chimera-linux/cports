pkgname = "knotifications"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "libcanberra-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Desktop notifications"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/knotifications/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/knotifications-{pkgver}.tar.xz"
sha256 = "36b7881d50400f37b4f3aeaa4c0a6a943e5783d35441e2b0cacdc6dad06af2a1"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/BSD-3-Clause.txt")


@subpackage("knotifications-devel")
def _(self):
    return self.default_devel()
