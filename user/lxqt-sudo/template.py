pkgname = "lxqt-sudo"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl"]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "GUI frontend for sudo/su"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-sudo"
source = f"{url}/releases/download/{pkgver}/lxqt-sudo-{pkgver}.tar.xz"
sha256 = "589e298b7165354feeeb7401e4595da07409498faa6e4d42697f435acab1cc72"
