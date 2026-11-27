pkgname = "lxqt-wayland-session"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "lxqt-build-tools", "ninja", "pkgconf", "perl"]
makedepends = [
    "kwindowsystem-devel",
    "liblxqt-devel",
    "qt6-qttools-devel",
    "xdg-user-dirs",
]
depends = ["qtxdg-tools", "layer-shell-qt", "lxqt-session"]
pkgdesc = "Files needed for the LXQt Wayland Session"
license = "LGPL-2.1-or-later AND MIT AND BSD-3-Clause AND GPL-3.0-only AND GPL-2.0-only AND CC-BY-SA-4.0"
url = "https://github.com/lxqt/lxqt-wayland-session"
source = (
    f"{url}/releases/download/{pkgver}/lxqt-wayland-session-{pkgver}.tar.xz"
)
sha256 = "05f96b6cc27bebfe7776bb62d5375266a310f40996295d0887c3a0c451d21d67"


def post_install(self):
    self.install_license("LICENSE")
