pkgname = "lxqt-admin"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl"]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "polkit-qt-1-devel",
    "qt6-qttools-devel",
]
pkgdesc = "LXQt system administration tool"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-admin"
source = f"{url}/releases/download/{pkgver}/lxqt-admin-{pkgver}.tar.xz"
sha256 = "3e3776892832415a693fb9fc82e886f73a1c98bd60720e7825a32cdf0cebff23"
