pkgname = "lxqt-notificationd"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DLXQT_NOTIFICATION_BUILD_TESTS=ON"]
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
]
makedepends = [
    "kwindowsystem-devel",
    "layer-shell-qt-devel",
    "liblxqt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "LXQt notification daemon"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-notificationd"
source = f"{url}/releases/download/{pkgver}/lxqt-notificationd-{pkgver}.tar.xz"
sha256 = "e79e4d57b345333aa350ff8a1dfb8cd9e624beb6910a276c454b459cf580964b"
