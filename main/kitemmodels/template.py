pkgname = "kitemmodels"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE's item models extending the Qt model-view framework"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only AND LGPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kitemmodels/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kitemmodels-{pkgver}.tar.xz"
sha256 = "0aa0205323baf2d519ebb8f96ce7ed5524a8164a7440d905f977418bfbe6d349"
hardening = ["vis"]


@subpackage("kitemmodels-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
