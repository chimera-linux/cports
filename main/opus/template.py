pkgname = "opus"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-float-approx"]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
pkgdesc = "Totally open, royalty-free, highly versatile audio codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.opus-codec.org"
source = f"https://archive.mozilla.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "65b58e1e25b2a114157014736a3d9dfeaad8d41be1c8179866f144a2fb44ff9d"
# FIXME int
hardening = ["vis", "cfi", "!int"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("opus-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
