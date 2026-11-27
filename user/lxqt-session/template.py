pkgname = "lxqt-session"
pkgver = "2.5.0"
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
sha256 = "a9b65cb5ebe0ab9461f01d5810d9ccbd6ca849b60623a149113921b520c66e3f"
options = ["etcfiles"]
