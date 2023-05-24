pkgname = "libxslt"
pkgver = "1.1.34"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["docbook-xml", "docbook-xsl-nons", "pkgconf"]
makedepends = ["libxml2-devel", "libgcrypt-devel"]
pkgdesc = "GNOME XSLT parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xmlsoft.org/XSLT"
source = f"http://xmlsoft.org/sources/{pkgname}-{pkgver}.tar.gz"
sha256 = "98b1bd46d6792925ad2dfe9a87452ea2adebf69dcb9919ffd55bf926a7f93f7f"
# test code seemingly incompatible with current libxml2
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxslt-devel")
def _devel(self):
    return self.default_devel()


@subpackage("xsltproc")
def _xsltproc(self):
    self.pkgdesc = "XSLT 1.0 command line processor"
    return self.default_progs()


configure_gen = []
