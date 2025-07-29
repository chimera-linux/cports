pkgname = "lxqt-globalkeys"
pkgver = "2.2.0"
pkgrel = 1
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
sha256 = "66cfdfeed4c0b968f4635847ccc32bec8136bb74cfbd9a5b31e0475339f9979a"


@subpackage("lxqt-globalkeys-devel")
def _(self):
    return self.default_devel()
