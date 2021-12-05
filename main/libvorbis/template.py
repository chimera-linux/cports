pkgname = "libvorbis"
pkgver = "1.3.7"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libogg-devel"]
pkgdesc = "Vorbis general audio compression codec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.xiph.org/vorbis"
source = f"https://downloads.xiph.org/releases/vorbis/{pkgname}-{pkgver}.tar.xz"
sha256 = "b33cc4934322bcbf6efcbacf49e3ca01aadbea4114ec9589d1b1e9d20f72954b"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libvorbis-static")
def _static(self):
    return self.default_static()

@subpackage("libvorbis-devel")
def _devel(self):
    return self.default_devel(man = True, extra = ["usr/share/doc"])
