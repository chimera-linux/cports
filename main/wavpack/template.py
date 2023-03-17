pkgname = "wavpack"
pkgver = "5.6.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Hybrid lossless audio compression"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.wavpack.com"
source = f"https://github.com/dbry/WavPack/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "af8035f457509c3d338b895875228a9b81de276c88c79bb2d3e31d9b605da9a9"

def post_install(self):
    self.install_license("COPYING")

@subpackage("wavpack-devel")
def _devel(self):
    return self.default_devel()

@subpackage("wavpack-progs")
def _devel(self):
    return self.default_progs()
