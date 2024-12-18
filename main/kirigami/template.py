pkgname = "kirigami"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "libomp-devel",
    "qt6-qtbase-private-devel",  # qguiapplication_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE's QtQuick based UI component set"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only"
url = "https://develop.kde.org/frameworks/kirigami"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kirigami-{pkgver}.tar.xz"
sha256 = "a3429c8bcf40e252d11b0a4c35a43c0433a9835ea1b333580707379b7b5c82c0"
hardening = ["vis"]


@subpackage("kirigami-devel")
def _(self):
    self.depends += ["libomp-devel", "qt6-qtdeclarative-devel"]
    return self.default_devel()
