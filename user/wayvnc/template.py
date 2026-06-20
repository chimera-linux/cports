pkgname = "wayvnc"
pkgver = "0.10.0"
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
sha256 = "fcfda018d0e07ec00a80071420c8cc2a75885dc6d5e55bb50a9b12353754338f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
