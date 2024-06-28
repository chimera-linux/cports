pkgname = "libxslt"
pkgver = "1.1.41"
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
makedepends = ["libgcrypt-devel", "libxml2-devel"]
pkgdesc = "GNOME XSLT parser library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xmlsoft.org/XSLT"
source = f"$(GNOME_SITE)/libxslt/{pkgver[:pkgver.rfind('.')]}/libxslt-{pkgver}.tar.xz"
sha256 = "3ad392af91115b7740f7b50d228cc1c5fc13afc1da7f16cb0213917a37f71bda"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxslt-devel")
def _devel(self):
    return self.default_devel(extra=["usr/lib/xsltConf.sh"])


@subpackage("xsltproc")
def _xsltproc(self):
    self.pkgdesc = "XSLT 1.0 command line processor"
    return self.default_progs()
