pkgname = "wayvnc"
pkgver = "0.9.1"
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
maintainer = "ttyyls <contact@behri.org>"
license = "ISC"
url = "https://github.com/any1/wayvnc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aaaca02d36e54ec6ecf457dc266251946d895ac91521fbabb3470c3c09b3753c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
