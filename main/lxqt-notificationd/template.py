pkgname = "lxqt-notificationd"
pkgver = "2.1.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-notificationd"
source = f"{url}/releases/download/{pkgver}/lxqt-notificationd-{pkgver}.tar.xz"
sha256 = "7e17acbe1eb0501aaceb5eda0f4b34d2e1b69c1d30639eef4d4d33d4f15ef058"
