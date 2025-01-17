pkgname = "minisign"
pkgver = "0.12"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libsodium-devel"]
pkgdesc = "File signing and signature verification tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://jedisct1.github.io/minisign"
source = (
    f"https://github.com/jedisct1/minisign/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "796dce1376f9bcb1a19ece729c075c47054364355fe0c0c1ebe5104d508c7db0"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
