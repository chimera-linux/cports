pkgname = "qt6-qtwayland"
pkgver = "6.6.0"
pkgrel = 0
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
pkgdesc = "Qt6 Wayland component"
maintainer = "q66 <q66@chimera-linux.org>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwayland-everywhere-src-{pkgver}.tar.xz"
sha256 = "30c3d82d85d050c83370710a26d12c802199c51eba5c2726e9d6243edd03b7e8"
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
