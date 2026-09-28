pkgname = "lxqt-session"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
    "qtxdg-tools",
    "xdg-user-dirs",
]
makedepends = [
    "kwindowsystem-devel",
    "layer-shell-qt-devel",
    "liblxqt-devel",
    "procps-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
depends = [
    "qtxdg-tools",
    "xdg-user-dirs",
]
pkgdesc = "LXQt session manager"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-session"
source = f"{url}/releases/download/{pkgver}/lxqt-session-{pkgver}.tar.xz"
sha256 = "d77f378ece0bfc7195f1964e88f55919729c3b0a55a858d7155ffaacc57bba44"
options = ["etcfiles"]
