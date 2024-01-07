pkgname = "libraw"
pkgver = "0.21.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "zlib-devel",
    "jasper-devel",
    "libjpeg-turbo-devel",
    "lcms2-devel",
]
pkgdesc = "Raw image decoder library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only OR CDDL-1.0"
url = "https://libraw.org"
source = f"{url}/data/LibRaw-{pkgver}.tar.gz"
sha256 = "fe7288013206854baf6e4417d0fb63ba4ed7227bf36fff021992671c2dd34b03"


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("libraw-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libraw-progs")
def _progs(self):
    return self.default_progs()
