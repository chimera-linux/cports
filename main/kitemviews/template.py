pkgname = "kitemviews"
pkgver = "6.19.0"
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
sha256 = "d5865512eee33997e97b766acaccb32236b93e0f81a1a7912065cc7c02b3f252"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kitemviews-devel")
def _(self):
    return self.default_devel()
