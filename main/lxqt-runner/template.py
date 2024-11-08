pkgname = "lxqt-runner"
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
sha256 = "2b7f233792099d0ee2369576c5f2e0ebb3dce9137593e7cdf0a1ffe10feff6a6"
