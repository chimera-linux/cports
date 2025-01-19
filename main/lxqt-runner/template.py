pkgname = "lxqt-runner"
pkgver = "2.1.1"
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
sha256 = "bc764f027bcd3e40d5fa3c28b31db975aa8c1f5f75218384c5b1b3b37f8cbb5e"
