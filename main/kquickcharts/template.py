pkgname = "kquickcharts"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "spirv-tools"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "QtQuick high-performance charts module"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kquickcharts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kquickcharts-{pkgver}.tar.xz"
sha256 = "50f0470e961f95fab75cb4ae888bdd4239b462f187d725a476ef1ba0ce6af435"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _(self):
    return self.default_devel()
