pkgname = "cage"
pkgver = "0.1.5"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["wayland-protocols", "wlroots0.16-devel"]
pkgdesc = "Kiosk compositor for Wayland"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://www.hjdskes.nl/projects/cage"
source = f"https://github.com/cage-kiosk/cage/releases/download/v{pkgver}/cage-{pkgver}.tar.gz"
sha256 = "ece0312e559289df0238289ea6c60e9fed32d27fe3ae8a8f83eeff26ddc239e1"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
