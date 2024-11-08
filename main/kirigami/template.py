pkgname = "kirigami"
pkgver = "6.8.0"
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
sha256 = "0e0b90ac96ba49630e2c01d8977bd8c51c9ab1808313fc88f60de179700742a2"
hardening = ["vis"]


@subpackage("kirigami-devel")
def _(self):
    self.depends += ["libomp-devel", "qt6-qtdeclarative-devel"]
    return self.default_devel()
