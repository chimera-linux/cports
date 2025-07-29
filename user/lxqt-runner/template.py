pkgname = "lxqt-runner"
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
    "layer-shell-qt-devel",
    "liblxqt-devel",
    "lxqt-globalkeys-devel",
    "muparser-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Tool used to launch programs quickly by typing their names"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-runner"
source = f"{url}/releases/download/{pkgver}/lxqt-runner-{pkgver}.tar.xz"
sha256 = "e15caab4c9bc4e95b147095310ec4ed85553a906e1d4381067460b63a286e890"
