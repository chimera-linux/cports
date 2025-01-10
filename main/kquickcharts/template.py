pkgname = "kquickcharts"
pkgver = "6.10.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kquickcharts-{pkgver}.tar.xz"
sha256 = "a2036f7b1ee7abb9c278c7822fc18723d661d856da9dbf9f006ceebed731598f"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _(self):
    return self.default_devel()
