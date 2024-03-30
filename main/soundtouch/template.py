pkgname = "soundtouch"
pkgver = "2.3.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-openmp"]
configure_gen = ["./bootstrap"]
make_build_args = ["V=1"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["libomp-devel"]
pkgdesc = "SoundTouch audio processing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://www.surina.net/soundtouch"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "43b23dfac2f64a3aff55d64be096ffc7b73842c3f5665caff44975633a975a99"


@subpackage("soundtouch-devel")
def _devel(self):
    return self.default_devel()
