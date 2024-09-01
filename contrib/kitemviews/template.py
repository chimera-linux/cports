pkgname = "kitemviews"
pkgver = "6.5.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://api.kde.org/frameworks/kitemviews/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kitemviews-{pkgver}.tar.xz"
sha256 = "07f3b3880597995a9bbc3c9bc47dba2bcd924ec503b423ed8566e7e805cbb69c"
hardening = ["vis"]
# fails
options = ["!cross"]


@subpackage("kitemviews-devel")
def _(self):
    return self.default_devel()
