pkgname = "libva-utils"
pkgver = "2.20.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddrm=true", "-Dx11=true", "-Dwayland=true"]
hostmakedepends = ["pkgconf", "meson", "ninja"]
makedepends = ["libva-devel", "libdrm-devel", "libx11-devel"]
pkgdesc = "Collection of utilities for libva"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://github.com/intel/libva-utils"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1a5e3c3c24677a6b4bbee21042c4c06b0a2c62e56ebb1baa4e712392b5c72f9b"


def post_install(self):
    self.install_license("COPYING")
