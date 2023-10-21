pkgname = "kirigami"
pkgver = "6.2.1"
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
sha256 = "910412770e79b9c13ddac42199fa7511770cd9485b8f5a264e1ef6363a330c99"
# FIXME: cfi breaks at least kcmutils' kcmloadtest
hardening = ["vis", "!cfi"]


@subpackage("kirigami-devel")
def _devel(self):
    return self.default_devel()
