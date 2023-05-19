pkgname = "libndp"
pkgver = "1.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Library for Neighbor Discovery Protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "http://libndp.org"
source = f"{url}/files/{pkgname}-{pkgver}.tar.gz"
sha256 = "88ffb66ee2eb527f146f5c02f5ccbc38ba97d2b0d57eb46bfba488821ab0c02b"
# FIXME cfi
hardening = ["vis", "!cfi"]

@subpackage("libndp-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libndp-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []
