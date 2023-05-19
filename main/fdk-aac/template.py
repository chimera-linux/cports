pkgname = "fdk-aac"
pkgver = "2.0.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Fraunhofer FDK AAC library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:FDK-AAC"
url = "http://www.iis.fraunhofer.de/en/ff/amm/impl/fdkaaccodec.html"
source = f"$(SOURCEFORGE_SITE)/opencore-amr/{pkgname}-{pkgver}.tar.gz"
sha256 = "c9e8630cf9d433f3cead74906a1520d2223f89bcd3fa9254861017440b8eb22f"

def post_install(self):
    self.install_license("NOTICE")

@subpackage("fdk-aac-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
