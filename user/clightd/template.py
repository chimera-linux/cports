pkgname = "clightd"
# TODO: Can't build 5.9 yet as it requires libiio, which is missing
pkgver = "5.8"
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
    "dbus-devel",
    "elogind-devel",
    "libdrm-devel",
    "libjpeg-turbo-devel",
    "libmodule-devel",
    "libxrandr-devel",
    "linux-headers",
    "ninja",
    "pkgconf",
    "polkit-devel",
    "udev-devel",
    "wayland-devel",
]
pkgdesc = "Linux bus interface that lets you change screen brightness"
# , compute captured webcam frames brightness and change screen temperature"
maintainer = "Anthony <w732qq@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/FedeDP/Clightd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "89f0906bc2c1dd4f9bd62194499fd156197c211760c4bb1adcb149650f852684"


def post_install(self):
    self.install_service(self.files_path / "clightd")
