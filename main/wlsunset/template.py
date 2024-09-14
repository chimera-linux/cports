pkgname = "wlsunset"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "scdoc"]
makedepends = ["wayland-devel", "wayland-protocols"]
pkgdesc = "Day/night gamma adjustments for Wayland"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://git.sr.ht/~kennylevinsen/wlsunset"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a86ffb1793fe622802ec25795b69df864715986ecc175f7734e739c9e264ed72"
# FIXME int: recalc_stops() fails NullabilityReturn
hardening = ["!int", "vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
