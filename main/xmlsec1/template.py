pkgname = "xmlsec1"
pkgver = "1.3.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-docs", "--enable-http"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gnutls-devel"]
makedepends = [
    "gnutls-devel",
    "libgcrypt-devel",
    "libgcrypt-devel",
    "libtool-devel",
    "libxslt-devel",
    "nspr-devel",
    "nss-devel",
]
pkgdesc = "XML Security Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.aleksey.com/xmlsec"
source = f"{url}/download/xmlsec1-{pkgver}.tar.gz"
sha256 = "952b626ad3f3be1a4598622dab52fdab2a8604d0837c1b00589f3637535af92f"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _(self):
    return self.default_devel()
