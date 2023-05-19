pkgname = "libraw"
pkgver = "0.21.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "zlib-devel", "jasper-devel", "libjpeg-turbo-devel", "lcms2-devel"
]
pkgdesc = "Raw image decoder library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only OR CDDL-1.0"
url = "https://libraw.org"
source = f"{url}/data/LibRaw-{pkgver}.tar.gz"
sha256 = "630a6bcf5e65d1b1b40cdb8608bdb922316759bfb981c65091fec8682d1543cd"

def post_install(self):
    self.install_license("COPYRIGHT")

@subpackage("libraw-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libraw-progs")
def _progs(self):
    return self.default_progs()
