pkgname = "minisign"
pkgver = "0.11"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libsodium-devel"]
pkgdesc = "File signing and signature verification tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://jedisct1.github.io/minisign"
source = f"https://github.com/jedisct1/minisign/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "74c2c78a1cd51a43a6c98f46a4eabefbc8668074ca9aa14115544276b663fc55"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
