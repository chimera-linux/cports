pkgname = "qt6-qtshadertools"
pkgver = "6.9.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "qt6-qtbase"]
makedepends = ["qt6-qtbase-private-devel"]
depends = [self.with_pkgver("qt6-qtshadertools-libs")]
pkgdesc = "Qt6 shader tools"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtshadertools-everywhere-src-{pkgver}.tar.xz"
sha256 = "4e1ed24cce0887fb4b6c7be4f150239853a29c330c9717f6bacfb6376f3b4b74"
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]


@subpackage("qt6-qtshadertools-libs")
def _(self):
    return self.default_libs()


@subpackage("qt6-qtshadertools-devel")
def _(self):
    self.depends += [
        self.parent,
        "spirv-tools",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
