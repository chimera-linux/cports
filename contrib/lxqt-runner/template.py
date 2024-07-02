pkgname = "lxqt-runner"
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
    "layer-shell-qt-devel",
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "muparser-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Tool used to launch programs quickly by typing their names"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-runner"
source = f"{url}/releases/download/{pkgver}/lxqt-runner-{pkgver}.tar.xz"
sha256 = "9f8031d780304d1c3b2c9b56a27744341c5e81d7cf2155bac959eaa6929e949c"
