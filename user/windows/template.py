pkgname = "windows"
pkgver = "1.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Window overview and selection for Wayland compositors"
license = "GPL-3.0-only"
url = "https://github.com/RadioNoiseE/windows"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b33bd3773d368d92b352bf62040bd020e62a633f5394948c284f273d9655c718"
hardening = [
    "vis",
    "cfi",
]
# no test
options = ["!check"]


def install(self):
    self.install_bin("windows")
    self.install_man("windows.1")
