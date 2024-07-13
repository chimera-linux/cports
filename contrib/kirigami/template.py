pkgname = "kirigami"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "libomp-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE's QtQuick based UI component set"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only"
url = "https://develop.kde.org/frameworks/kirigami"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kirigami-{pkgver}.tar.xz"
sha256 = "eca20cd9ce72d0eeb57bd5fba394f20d83bb4612ac4a4c23fb8ca74a93188c37"
# CFI: breaks at least kcmutils' kcmloadtest
hardening = ["vis", "!cfi"]


@subpackage("kirigami-devel")
def _devel(self):
    self.depends += ["qt6-qtdeclarative-devel"]
    return self.default_devel()
