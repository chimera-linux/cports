pkgname = "lxqt-session"
pkgver = "2.1.1"
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
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-session"
source = f"{url}/releases/download/{pkgver}/lxqt-session-{pkgver}.tar.xz"
sha256 = "312b0cd4106d0bca6812c7100750edee012e93e9fefc2b171731a782bc9bc819"
