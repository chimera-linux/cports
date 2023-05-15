pkgname = "qt6-qtsvg"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_BUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "qt6-qtbase"]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Qt6 SVG component"
license = "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtsvg-everywhere-src-{pkgver}.tar.xz"
sha256 = "64ca7e61f44d51e28bcbb4e0509299b53a9a7e38879e00a7fe91643196067a4f"
debug_level = 1 # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive = True)

@subpackage("qt6-qtsvg-devel")
def _devel(self):
    return self.default_devel(extra = [
        "usr/lib/qt6/metatypes",
        "usr/lib/qt6/mkspecs",
        "usr/lib/qt6/modules",
        "usr/lib/*.prl",
    ])
