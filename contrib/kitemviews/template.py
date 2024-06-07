pkgname = "kitemviews"
pkgver = "6.3.0"
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
sha256 = "d8657d155611631834a800a6fb0aac110b6baa4435de00fbd6048bd9f1a2d42f"
hardening = ["vis", "!cfi"]
# fails
options = ["!cross"]


@subpackage("kitemviews-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
