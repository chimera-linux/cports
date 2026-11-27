pkgname = "lxqt-policykit"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "perl", "pkgconf"]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "polkit-devel",
    "polkit-qt-1-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "LXQt PolicyKit agent"
license = "LGPL-2.0-or-later"
url = "https://github.com/lxqt/lxqt-policykit"
source = f"{url}/releases/download/{pkgver}/lxqt-policykit-{pkgver}.tar.xz"
sha256 = "a8c2e57c8c1952d327f945b3dd3725dbdf85dafc853e8d9bcae4f269362017e7"
options = ["etcfiles"]
