pkgname = "qt6-qtwayland"
pkgver = "6.7.2"
pkgrel = 2
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = ["-E", "(tst_seatv4|tst_client|tst_scaling|tst_compositor)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen", "XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = [
    "cmake",
    "ninja",
    "perl",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = ["qt6-qtbase-devel", "qt6-qtdeclarative-devel"]
checkdepends = ["mesa-dri"]
install_if = [self.with_pkgver("qt6-qtbase-gui"), "wayland"]
pkgdesc = "Qt6 Wayland component"
maintainer = "q66 <q66@chimera-linux.org>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwayland-everywhere-src-{pkgver}.tar.xz"
sha256 = "a2a057e1dd644bd44abb9990fecc194b2e25c2e0f39e81aa9fee4c1e5e2a8a5b"
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]


@subpackage("qt6-qtwayland-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/libexec",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
