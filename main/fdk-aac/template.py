pkgname = "fdk-aac"
pkgver = "2.0.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Fraunhofer FDK AAC library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:FDK-AAC"
url = "http://www.iis.fraunhofer.de/en/ff/amm/impl/fdkaaccodec.html"
source = f"$(SOURCEFORGE_SITE)/opencore-amr/{pkgname}-{pkgver}.tar.gz"
sha256 = "829b6b89eef382409cda6857fd82af84fabb63417b08ede9ea7a553f811cb79e"


def post_install(self):
    self.install_license("NOTICE")


@subpackage("fdk-aac-devel")
def _devel(self):
    return self.default_devel()
