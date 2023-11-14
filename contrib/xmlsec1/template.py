pkgname = "xmlsec1"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-docs"]
hostmakedepends = ["pkgconf", "automake", "libtool", "gnutls-devel"]
makedepends = [
    "libxslt-devel",
    "gnutls-devel",
    "libgcrypt-devel",
    "nspr-devel",
    "nss-devel",
    "libgcrypt-devel",
    "libltdl-devel",
]
pkgdesc = "XML Security Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.aleksey.com/xmlsec"
source = f"{url}/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "4003c56b3d356d21b1db7775318540fad6bfedaf5f117e8f7c010811219be3cf"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _dev(self):
    return self.default_devel()
