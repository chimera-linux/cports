pkgname = "qt6-qtwayland"
pkgver = "6.6.1"
pkgrel = 2
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = ["-E", "tst_seatv4$"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen", "XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = ["qt6-qtbase-devel", "qt6-qtdeclarative-devel"]
checkdepends = ["mesa-dri"]
install_if = [f"qt6-qtbase-gui={pkgver}-r{pkgrel}", "wayland"]
pkgdesc = "Qt6 Wayland component"
maintainer = "q66 <q66@chimera-linux.org>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwayland-everywhere-src-{pkgver}.tar.xz"
sha256 = "66cc2d632dc07fc6cc4e35247f48b7c1753276ccbf86e86d7b24d799725568b1"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]


@subpackage("qt6-qtwayland-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/libexec",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
