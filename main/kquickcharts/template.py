pkgname = "kquickcharts"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "spirv-tools"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "QtQuick high-performance charts module"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kquickcharts-{pkgver}.tar.xz"
sha256 = "2c2c18c1eb1ea1c8d9df0dc084bd2770b0099dc10cc0cb6827c7dc6bd5d3c21d"
hardening = ["vis"]


@subpackage("kquickcharts-devel")
def _(self):
    return self.default_devel()
