pkgname = "kirigami"
pkgver = "6.3.0"
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
sha256 = "dbcbfaa05b37c03501fe8f4dfaf92f6f7bf9b871b8d28897363a5678dcb2395b"
# FIXME: cfi breaks at least kcmutils' kcmloadtest
hardening = ["vis", "!cfi"]


@subpackage("kirigami-devel")
def _devel(self):
    self.depends += ["qt6-qtdeclarative-devel"]
    return self.default_devel()
