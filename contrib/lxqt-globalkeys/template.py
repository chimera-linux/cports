pkgname = "lxqt-globalkeys"
pkgver = "2.0.0"
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
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-globalkeys"
source = f"{url}/releases/download/{pkgver}/lxqt-globalkeys-{pkgver}.tar.xz"
sha256 = "13e7a72686890a40b65d8ae13c79ed287eb971fbc0285769c40c8b97e7af43f7"


@subpackage("lxqt-globalkeys-devel")
def _(self):
    return self.default_devel()
