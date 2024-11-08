pkgname = "lxqt-globalkeys"
pkgver = "2.1.0"
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
sha256 = "70cc56c452626a2c3ceb7ade8745ed61bac10c7d9aa082443a74aba1e3942874"


@subpackage("lxqt-globalkeys-devel")
def _(self):
    return self.default_devel()
