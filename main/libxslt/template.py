pkgname = "libxslt"
pkgver = "1.1.39"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-python=no"]
hostmakedepends = [
    "automake",
    "docbook-xml",
    "docbook-xsl-nons",
    "libtool",
    "pkgconf",
]
makedepends = ["libxml2-devel", "libgcrypt-devel"]
pkgdesc = "GNOME XSLT parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xmlsoft.org/XSLT"
source = f"$(GNOME_SITE)/libxslt/{pkgver[:pkgver.rfind('.')]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2a20ad621148339b0759c4d4e96719362dee64c9a096dbba625ba053846349f0"
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
