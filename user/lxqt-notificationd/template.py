pkgname = "lxqt-notificationd"
pkgver = "2.5.0"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-notificationd"
source = f"{url}/releases/download/{pkgver}/lxqt-notificationd-{pkgver}.tar.xz"
sha256 = "d45a21024aad071e0b364c50a7e78b3fbb3f5145dd58a4762b50fde905d0ba2a"
options = ["etcfiles"]
