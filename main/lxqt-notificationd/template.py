pkgname = "lxqt-notificationd"
pkgver = "2.0.1"
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
sha256 = "f66366221825774967b4ae4ec658d00128bf4536be779ca02e4406a184262aec"
