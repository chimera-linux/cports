pkgname = "xdg-desktop-portal-lxqt"
pkgver = "1.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja"]
makedepends = [
    "kwindowsystem-devel",
    "libexif-devel",
    "libfm-qt-devel",
    "qt6-qtbase-devel",
    "xdg-desktop-portal-devel",
]
depends = ["xdg-desktop-portal"]
pkgdesc = "LXQT xdg desktop portal"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/xdg-desktop-portal-lxqt"
source = (
    f"{url}/releases/download/{pkgver}/xdg-desktop-portal-lxqt-{pkgver}.tar.xz"
)
sha256 = "ce8c222e0849ad581d86f22609f37ac0cd391443313807bf9a2e0b3b894e971f"


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
