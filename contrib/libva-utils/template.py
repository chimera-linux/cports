pkgname = "libva-utils"
pkgver = "2.17.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddrm=true", "-Dx11=true", "-Dwayland=true"]
hostmakedepends = ["pkgconf", "meson", "ninja"]
makedepends = ["libva-devel", "libdrm-devel", "libx11-devel"]
pkgdesc = "Collection of utilities for libva"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://github.com/intel/libva-utils"
source = f"https://github.com/intel/libva-utils/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6ea5993c3eba230a979fa9d35b4cad8df06d4474a773dc0918033bf50353f966"
