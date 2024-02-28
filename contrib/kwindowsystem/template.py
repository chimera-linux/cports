pkgname = "kwindowsystem"
pkgver = "6.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_MAJOR_VERSION=6",
]
make_check_args = [
    "-E",
    # FIXME: hangs/crashes
    "(threadtest|compositingenabled|kwindowinfox11test|kwindowsystemx11test|netrootinfotestwm)",
]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "libxrender-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "KDE windowing system access"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/frameworks/kwindowsystem"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kwindowsystem-{pkgver}.tar.xz"
sha256 = "1906caa53b7d58fc0c4d78a3c8d99f25aa056fc6d09c5fc121ed5e1f80396a94"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("kwindowsystem-devel")
def _devel(self):
    return self.default_devel()
