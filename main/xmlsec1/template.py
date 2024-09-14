pkgname = "xmlsec1"
pkgver = "1.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-docs", "--enable-http"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gnutls-devel"]
makedepends = [
    "gnutls-devel",
    "libgcrypt-devel",
    "libgcrypt-devel",
    "libltdl-devel",
    "libxslt-devel",
    "nspr-devel",
    "nss-devel",
]
pkgdesc = "XML Security Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.aleksey.com/xmlsec"
source = f"{url}/download/xmlsec1-{pkgver}.tar.gz"
sha256 = "2ffd4ad1f860ec93e47a680310ab2bc94968bd07566e71976bd96133d9504917"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _(self):
    return self.default_devel()
