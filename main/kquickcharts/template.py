pkgname = "kquickcharts"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "spirv-tools",
]
makedepends = [
    "qt6-qtdeclarative-devel",
]
pkgdesc = "QtQuick high-performance charts module"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kquickcharts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kquickcharts-{pkgver}.tar.xz"
sha256 = "d8441008d625763bf7b20a8b1685d09cd69416c6ce4603743e93c16fc5397a47"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _(self):
    return self.default_devel()
