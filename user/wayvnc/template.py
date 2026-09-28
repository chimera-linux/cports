pkgname = "wayvnc"
pkgver = "0.10.1"
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
sha256 = "1dcb54f58d1637995bfb59c17709efca7833bae41f31b33eb47e608668a89d66"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
