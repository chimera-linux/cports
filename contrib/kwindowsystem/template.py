pkgname = "kwindowsystem"
pkgver = "5.112.0"
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
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "libxrender-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
]
checkdepends = ["xserver-xorg-xvfb"]
pkgdesc = "KDE windowing system access"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/frameworks/kwindowsystem"
source = f"https://download.kde.org/stable/frameworks/{pkgver[:pkgver.rfind('.')]}/kwindowsystem-{pkgver}.tar.xz"
sha256 = "418e13e52f66a4030757d8479c787adab1112f40f694c0cc26309d84bf793022"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("kwindowsystem-devel")
def _devel(self):
    return self.default_devel()
