pkgname = "qt6-qtwebchannel"
pkgver = "6.7.1"
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
    "qt6-qtwebsockets-devel",
]
pkgdesc = "Qt6 webchannel component"
maintainer = "psykose <alice@ayaya.dev>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwebchannel-everywhere-src-{pkgver}.tar.xz"
sha256 = "b9d995edfce90bce04635305936e49a8ae61196d74bcce0f09d26b285d2dcc6f"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# literally doesn't find itself for some byzantine reason
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive=True)


@subpackage("qt6-qtwebchannel-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
