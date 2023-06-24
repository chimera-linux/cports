pkgname = "wlsunset"
pkgver = "0.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["wayland-devel", "wayland-protocols"]
pkgdesc = "Day/night gamma adjustments for Wayland"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://git.sr.ht/~kennylevinsen/wlsunset"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "9ece2570c3427888a493cd33a129e82634475e6e9286ed729af24fba07ab5424"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
