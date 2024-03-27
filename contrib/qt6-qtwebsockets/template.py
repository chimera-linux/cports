pkgname = "qt6-qtwebsockets"
pkgver = "6.6.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Qt6 websockets component"
maintainer = "psykose <alice@ayaya.dev>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwebsockets-everywhere-src-{pkgver}.tar.xz"
sha256 = "16f481765794dd66e4538a1074fbc9a68e2091eda5f99868cc27d9b1a931a036"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# literally doesn't find itself for some byzantine reason
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive=True)


@subpackage("qt6-qtwebsockets-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
