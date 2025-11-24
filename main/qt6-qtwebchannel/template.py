pkgname = "qt6-qtwebchannel"
pkgver = "6.10.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebsockets-devel",
]
pkgdesc = "Qt6 webchannel component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwebchannel-everywhere-src-{pkgver}.tar.xz"
sha256 = "7ba16925f230e60f58efce02c1ce214bcb6b0740e24f5dd40c06f40f37d93111"
# FIXME
hardening = ["!int"]
# literally doesn't find itself for some byzantine reason
options = ["!check"]


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtwebchannel-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
