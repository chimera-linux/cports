pkgname = "clightd"
pkgver = "5.9"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DDBUS_CONFIG_DIR=/usr/share/dbus-1/system.d/",
    "-DENABLE_DPMS=1",
    "-DENABLE_GAMMA=1",
    "-DENABLE_SCREEN=1",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "elogind-devel",
    "libdrm-devel",
    "libiio-devel",
    "libjpeg-turbo-devel",
    "libmodule-devel",
    "libxrandr-devel",
    "linux-headers",
    "polkit-devel",
    "udev-devel",
    "wayland-devel",
]
pkgdesc = "Linux bus interface that lets you change screen brightness"
maintainer = "Anthony <w732qq@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/FedeDP/Clightd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "76ae865b5eeb721c98c23b1d4d8531b2b6c10b71386d0396b14666b5650f3054"


def post_install(self):
    self.install_service(self.files_path / "clightd")
