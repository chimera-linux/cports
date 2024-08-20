pkgname = "liblxqt"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kwindowsystem-devel",
    "libqtxdg-devel",
    "libxscrnsaver-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Core utility library for all LXQt components"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/liblxqt"
source = f"{url}/releases/download/{pkgver}/liblxqt-{pkgver}.tar.xz"
sha256 = "61092556146b769dc9bab328550f3f157e618a1a09ae1e052db61fc0db07b3e4"


@subpackage("liblxqt-devel")
def _(self):
    return self.default_devel()
