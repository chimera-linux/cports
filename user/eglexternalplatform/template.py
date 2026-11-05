pkgname = "eglexternalplatform"
pkgver = "1.2.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "EGL External Platform interface"
license = "MIT"
url = "https://github.com/NVIDIA/eglexternalplatform"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5089ceb054ca50c85837f015756a3d0f2f75cf2a98c9e5fbcbcfb8206137f76e"


def post_install(self):
    self.install_license("COPYING")
