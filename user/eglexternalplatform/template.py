pkgname = "eglexternalplatform"
pkgver = "1.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "EGL External Platform interface"
license = "MIT"
url = "https://github.com/NVIDIA/eglexternalplatform"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "aba414e6f441b1253684b4bb838b3fecde2a851374a71f32a7ba2ca80daf1709"


def post_install(self):
    self.install_license("COPYING")
