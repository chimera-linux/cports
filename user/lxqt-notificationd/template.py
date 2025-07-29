pkgname = "lxqt-notificationd"
pkgver = "2.2.0"
pkgrel = 1
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
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-notificationd"
source = f"{url}/releases/download/{pkgver}/lxqt-notificationd-{pkgver}.tar.xz"
sha256 = "4223bf6ce1c2e5f67020320c70f221c13c94b17b5e33fd00fd6f8e2983a779c4"
