pkgname = "libva-utils"
pkgver = "2.18.2"
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
sha256 = "c4c0555c96ca678f9ac47fbb56f0ae56ca39fd50fe3553bae5cb13117bfcb406"

def post_install(self):
    self.install_license("COPYING")
