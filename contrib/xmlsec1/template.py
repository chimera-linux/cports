pkgname = "xmlsec1"
pkgver = "1.3.0"
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
sha256 = "df3ad2548288411fc3d44c20879e4c4e90684a1a4fb76a06ae444f957171c9a6"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


@subpackage("xmlsec1-devel")
def _dev(self):
    return self.default_devel()
