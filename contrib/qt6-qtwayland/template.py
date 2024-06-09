pkgname = "qt6-qtwayland"
pkgver = "6.7.1"
pkgrel = 7
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = ["-E", "(tst_seatv4|tst_client|tst_scaling|tst_compositor)"]
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
sha256 = "7ef176a8e701c90edd8e591dad36f83c30d623ef94439ff62cafcffd46a83d20"
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
