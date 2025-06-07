pkgname = "libva-utils"
pkgver = "2.22.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddrm=true", "-Dx11=true", "-Dwayland=true"]
hostmakedepends = ["pkgconf", "meson"]
makedepends = ["libva-devel", "libdrm-devel", "libx11-devel"]
pkgdesc = "Collection of utilities for libva"
license = "MIT"
url = "https://github.com/intel/libva-utils"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7b57615c130427ec134bb5d2b80af516ce5bb19a40e89b1dab46a0d59760d96c"


def post_install(self):
    self.install_license("COPYING")
