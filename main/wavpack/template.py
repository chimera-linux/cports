pkgname = "wavpack"
pkgver = "5.5.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Hybrid lossless audio compression"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.wavpack.com"
source = f"https://github.com/dbry/WavPack/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ef749d98df46925bc2916993e601cc7ee9114d99653e63e0e304f031ba73b8e6"

def post_install(self):
    self.install_license("COPYING")

@subpackage("wavpack-devel")
def _devel(self):
    return self.default_devel()

@subpackage("wavpack-progs")
def _devel(self):
    return self.default_progs()

# FIXME visibility
hardening = ["!vis"]
