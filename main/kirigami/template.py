pkgname = "kirigami"
pkgver = "6.7.0"
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
sha256 = "4d645a0374d33b9465e79e3e17170882e2cbda1526f45bc5b6b176dadda77d76"
hardening = ["vis"]


@subpackage("kirigami-devel")
def _(self):
    self.depends += ["libomp-devel", "qt6-qtdeclarative-devel"]
    return self.default_devel()
