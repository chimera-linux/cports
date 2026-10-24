pkgname = "wayvnc"
pkgver = "0.10.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "jansson-devel",
    "libdrm-devel",
    "libxkbcommon-devel",
    "mesa-gbm-devel",
    "musl-bsd-headers",
    "neatvnc-devel",
    "pixman-devel",
    "wayland-devel",
]
pkgdesc = "VNC server for wlroots-based Wayland compositors"
license = "ISC"
url = "https://github.com/any1/wayvnc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a85c6556a249b631551213f1e0fc20861458aea381996fd30a11fea431a465f9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
