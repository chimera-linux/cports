pkgname = "soundtouch"
pkgver = "2.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-openmp"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libomp-devel"]
pkgdesc = "SoundTouch audio processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.surina.net/soundtouch"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6900996607258496ce126924a19fe9d598af9d892cf3f33d1e4daaa9b42ae0b1"

def pre_configure(self):
    self.do(self.chroot_cwd / "bootstrap")

@subpackage("soundtouch-devel")
def _devel(self):
    return self.default_devel()
