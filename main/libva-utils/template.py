pkgname = "libva-utils"
pkgver = "2.20.1"
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
sha256 = "97413a7ec27ec479b97ffc7ab8acebe053615224a4b051602859cf9f88e4e889"


def post_install(self):
    self.install_license("COPYING")
