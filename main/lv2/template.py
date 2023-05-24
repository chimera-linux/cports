pkgname = "lv2"
pkgver = "1.18.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Plugin standard for audio systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://lv2plug.in"
source = f"{url}/spec/{pkgname}-{pkgver}.tar.xz"
sha256 = "78c51bcf21b54e58bb6329accbb4dae03b2ed79b520f9a01e734bd9de530953f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
