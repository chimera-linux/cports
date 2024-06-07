pkgname = "kitemmodels"
pkgver = "6.3.0"
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
sha256 = "b3a984fb62919c1f8bb3fb77a2e207e51a52f5c596415ea9fc8ffa618b56acba"
hardening = ["vis", "!cfi"]


@subpackage("kitemmodels-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
