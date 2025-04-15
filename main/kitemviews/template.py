pkgname = "kitemviews"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Widget addons for Qt Model/View"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://api.kde.org/frameworks/kitemviews/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kitemviews-{pkgver}.tar.xz"
sha256 = "e0de8c9fa2baa27bde6abd3847b6d5f4cb54aeceab3436c64f89a50fe1d9695d"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kitemviews-devel")
def _(self):
    return self.default_devel()
