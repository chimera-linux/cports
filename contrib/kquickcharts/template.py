pkgname = "kquickcharts"
pkgver = "6.3.0"
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
sha256 = "250e522adfbf48b3f2763f4ec378a20337a1ca2e5b0e2cd8b3615d7a3fed8fc7"
# FIXME: cfi crashes plasma-systemmonitor on launch in libQuickChartsControls.so
hardening = ["vis", "!cfi"]


@subpackage("kquickcharts-devel")
def _devel(self):
    return self.default_devel()
