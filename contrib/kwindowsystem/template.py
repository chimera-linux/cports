pkgname = "kwindowsystem"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # kwindowinfox11test takes over 5 minutes and is broken,
    # threadtest & kwindowsystemx11test are broken,
    # netrootinfotestwm fails on ppc64le
    "((thread|kwindowsystemx11|kwindowinfox11)test|netrootinfotestwm)",
    # at least compositingenabled_test is flaky when parallel
    "-j1",
]
make_check_env = {"QT_QPA_PLATFORM": "xcb"}
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
checkdepends = [
    "xserver-xorg-xvfb",
]
depends = [
    "qqc2-desktop-style",
]
pkgdesc = "KDE windowing system access"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://invent.kde.org/frameworks/kwindowsystem"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kwindowsystem-{pkgver}.tar.xz"
sha256 = "40e33c592934bc27484b922e3dab3c9fdbe078063fa5bcaf29d50d2cd8e8aab9"
# CFI: breaks at least kwin testDontCrashUseractionsMenu
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("kwindowsystem-devel")
def _devel(self):
    return self.default_devel()
