pkgname = "lxqt-runner"
pkgver = "2.5.0"
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
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-runner"
source = f"{url}/releases/download/{pkgver}/lxqt-runner-{pkgver}.tar.xz"
sha256 = "f9c6b9eb9e1f91f6669436e5cf5e1fd5bcfe279eca75c2f9779b9115aad8108c"
options = ["etcfiles"]
