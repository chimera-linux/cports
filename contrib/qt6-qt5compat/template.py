pkgname = "qt6-qt5compat"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qtbase"]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Module containing unsuppored Qt5 APIs"
maintainer = "aurelia <git@elia.garden>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qt5compat-everywhere-src-{pkgver}.tar.xz"
sha256 = "a9e2f53a193fc2e131b01a2f6e7a1fbfe31309c2413fdc213e5a81c558c21261"
# TODO
options = ["!check"]


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
