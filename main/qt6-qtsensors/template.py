pkgname = "qt6-qtsensors"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Qt6 Sensors component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtsensors-everywhere-src-{pkgver}.tar.xz"
sha256 = "67525e1ad1833ce556a208c4fd8adc59fe6e20d9450e621977ade96300668739"
# TODO
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/cmake/Qt6BuildInternals")
    self.uninstall("usr/tests")


@subpackage("qt6-qtsensors-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
