pkgname = "wavpack"
pkgver = "5.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Hybrid lossless audio compression"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.wavpack.com"
source = f"https://github.com/dbry/WavPack/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4bde6a6b2a86614a6bd2579e60dcc974e2c8f93608d2281110a717c1b3c28b79"

def post_install(self):
    self.install_license("COPYING")

@subpackage("wavpack-devel")
def _devel(self):
    return self.default_devel()

@subpackage("wavpack-progs")
def _devel(self):
    return self.default_progs()
