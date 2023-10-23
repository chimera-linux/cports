pkgname = "qt6-qtsensors"
pkgver = "6.7.1"
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
sha256 = "d5694a17d90f71039c12daf9c1c14fd76baf447246798e7cad171038c80dfbf2"
# TODO
options = ["!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/cmake/Qt6BuildInternals", recursive=True)
    self.rm(self.destdir / "usr/tests", recursive=True)


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
