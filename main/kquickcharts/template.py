pkgname = "kquickcharts"
pkgver = "6.20.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "spirv-tools"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "QtQuick high-performance charts module"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kquickcharts/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kquickcharts-{pkgver}.tar.xz"
sha256 = "94f52ce42c15cb7dc514ce9868dba41ed8f0645b941ff2256d02227746301792"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _(self):
    return self.default_devel()
