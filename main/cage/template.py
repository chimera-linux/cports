pkgname = "cage"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["wayland-protocols", "wlroots0.18-devel"]
pkgdesc = "Kiosk compositor for Wayland"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://www.hjdskes.nl/projects/cage"
source = f"https://github.com/cage-kiosk/cage/releases/download/v{pkgver}/cage-{pkgver}.tar.gz"
sha256 = "557c194d18af7202a9ec2e8be6dd7129f6c16d0f4528f4079ba26ccd57b6ef88"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
