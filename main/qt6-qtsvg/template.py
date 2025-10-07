pkgname = "qt6-qtsvg"
pkgver = "6.10.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = ["-E", "module_includes"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "qt6-qtbase"]
makedepends = ["qt6-qtbase-private-devel"]
pkgdesc = "Qt6 SVG component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtsvg-everywhere-src-{pkgver}.tar.xz"
sha256 = "5ed2c0e04d5e73ff75c2a2ed92db5dc1788ba70f704fc2b71bc21644beda2533"
# FIXME
hardening = ["!int"]


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtsvg-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
