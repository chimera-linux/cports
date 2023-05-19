pkgname = "soundtouch"
pkgver = "2.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-openmp"]
make_build_args = ["V=1"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libomp-devel"]
pkgdesc = "SoundTouch audio processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.surina.net/soundtouch"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3bde8ddbbc3661f04e151f72cf21ca9d8f8c88e265833b65935b8962d12d6b08"

def pre_configure(self):
    self.do(self.chroot_cwd / "bootstrap")

@subpackage("soundtouch-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
