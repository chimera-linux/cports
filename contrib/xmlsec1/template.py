pkgname = "xmlsec1"
pkgver = "1.3.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-docs"]
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
source = f"{url}/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "45ad9078d41ae76844ad2f8651600ffeec0fdd128ead988a8d69e907c57aee75"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _devel(self):
    return self.default_devel()
