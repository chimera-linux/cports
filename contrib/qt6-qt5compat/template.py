pkgname = "qt6-qt5compat"
pkgver = "6.6.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qtbase"]
makedepends = ["qt6-qtdeclarative-devel"]
pkgdesc = "Module containing unsuppored Qt5 APIs"
maintainer = "aurelia <git@elia.garden>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qt5compat-everywhere-src-{pkgver}.tar.xz"
sha256 = "e07b08ab7658e4856f07e3262ab342df4ed7e7a69f2720e56bb2128729191967"
# TODO
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive=True)


@subpackage("qt6-qt5compat-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
