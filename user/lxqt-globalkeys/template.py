pkgname = "lxqt-globalkeys"
pkgver = "2.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Daemon used to register global keyboard shortcuts"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-globalkeys"
source = f"{url}/releases/download/{pkgver}/lxqt-globalkeys-{pkgver}.tar.xz"
sha256 = "6f7fb82337bd06823f698df5a1e631059e99e544bfa9a1d7c5b67fd01ff9319a"
options = ["etcfiles"]


@subpackage("lxqt-globalkeys-devel")
def _(self):
    return self.default_devel()
