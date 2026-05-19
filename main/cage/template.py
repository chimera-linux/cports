pkgname = "cage"
pkgver = "0.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["wayland-protocols", "wlroots0.20-devel"]
pkgdesc = "Kiosk compositor for Wayland"
license = "MIT"
url = "https://www.hjdskes.nl/projects/cage"
source = f"https://github.com/cage-kiosk/cage/releases/download/v{pkgver}/cage-{pkgver}.tar.gz"
sha256 = "cd2510f83bef3e08e660d99492ca7761b218ecb53ee01cdbbeee3d6aabc7734e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
