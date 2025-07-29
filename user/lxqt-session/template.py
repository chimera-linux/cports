pkgname = "lxqt-session"
pkgver = "2.2.0"
pkgrel = 1
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
sha256 = "27bc2613b516af503511f15f38216ef9650bc8f65ae6154990b76b1a20d3898a"
