pkgname = "cage"
pkgver = "0.3.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["wayland-protocols", "wlroots0.20-devel"]
pkgdesc = "Kiosk compositor for Wayland"
license = "MIT"
url = "https://www.hjdskes.nl/projects/cage"
source = f"https://github.com/cage-kiosk/cage/releases/download/v{pkgver}/cage-{pkgver}.tar.gz"
sha256 = "edafc173b6f56a3e1564933e272a54aaa9fe158d330e6a415d57b44ab880fe2b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
