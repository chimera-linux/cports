pkgname = "libva-utils"
pkgver = "2.23.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddrm=true", "-Dx11=true", "-Dwayland=true"]
hostmakedepends = ["pkgconf", "meson"]
makedepends = ["libva-devel", "libdrm-devel", "libx11-devel"]
pkgdesc = "Collection of utilities for libva"
license = "MIT"
url = "https://github.com/intel/libva-utils"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fa7ff29847b55010fbbb775b35382f97f29b7b97abe9a2f6fb3e22b36db5440a"


def post_install(self):
    self.install_license("COPYING")
