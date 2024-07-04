pkgname = "qt6-qtsensors"
pkgver = "6.7.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["qt6-qtdeclarative-devel", "qt6-qtsvg-devel"]
pkgdesc = "Qt6 Sensors component"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtsensors-everywhere-src-{pkgver}.tar.xz"
sha256 = "ead1dec787c56ed4dc02ed810af54ff1e1f6875cb5cc2506c74eeb9554e6bb59"
# TODO
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/cmake/Qt6BuildInternals")
    self.uninstall("usr/tests")


@subpackage("qt6-qtsensors-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
