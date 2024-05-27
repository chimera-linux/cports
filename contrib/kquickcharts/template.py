pkgname = "kquickcharts"
pkgver = "6.2.0"
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
sha256 = "fdd96bf4218a309be28523ac318bd7816e8bd1febf0e771b13359cd658c6756b"
# FIXME: cfi crashes plasma-systemmonitor on launch in libQuickChartsControls.so
hardening = ["vis", "!cfi"]


@subpackage("kquickcharts-devel")
def _devel(self):
    return self.default_devel()
