pkgname = "lxqt-powermanagement"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl"]
makedepends = [
    "kidletime-devel",
    "kwindowsystem-devel",
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "solid-devel",
    "upower-devel",
]
pkgdesc = "Power management module for LXQt"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-powermanagement"
source = (
    f"{url}/releases/download/{pkgver}/lxqt-powermanagement-{pkgver}.tar.xz"
)
sha256 = "3d4a884ef0fc115f153fc631b3d0af811cb0201bc1ce1dcbb1919959f3429625"
options = ["etcfiles"]
