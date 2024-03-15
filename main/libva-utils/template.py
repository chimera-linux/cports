pkgname = "libva-utils"
pkgver = "2.21.0"
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
sha256 = "15ca12bd11c7001c04af5079512754fea6ba8d79151b9f07908c99b27622714e"


def post_install(self):
    self.install_license("COPYING")
