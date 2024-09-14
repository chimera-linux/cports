pkgname = "wtype"
pkgver = "0.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = ["libxkbcommon-devel", "wayland-devel"]
pkgdesc = "Xdotool type for wayland"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/atx/wtype"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "da91786d828b6a6e29b884bc510473939eda052658ebef87d7bdeafa6a8746f9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
