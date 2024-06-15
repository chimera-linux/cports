pkgname = "libxslt"
pkgver = "1.1.40"
pkgrel = 1
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
sha256 = "194715db023035f65fb566402f2ad2b5eab4c29d541f511305c40b29b1f48d13"
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
