pkgname = "kquickcharts"
pkgver = "6.4.0"
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
sha256 = "a41629caef3877ce03c739c0950f094890f5b2a20a041dd338bdeb240c6401de"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _devel(self):
    return self.default_devel()
