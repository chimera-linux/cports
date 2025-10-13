pkgname = "cage"
pkgver = "0.2.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["wayland-protocols", "wlroots0.19-devel"]
pkgdesc = "Kiosk compositor for Wayland"
license = "MIT"
url = "https://www.hjdskes.nl/projects/cage"
source = f"https://github.com/cage-kiosk/cage/releases/download/v{pkgver}/cage-{pkgver}.tar.gz"
sha256 = "fc1238e3aa5b82787a95d49cb3e1bac0671e4d3a40090087848f43f3e1f63a98"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
