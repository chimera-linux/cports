pkgname = "xmlsec1"
pkgver = "1.3.3"
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
sha256 = "ab5b9a9ffd6960f46f7466d9d91f174ec37e8c31989237ba6b9eacdd816464f2"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _dev(self):
    return self.default_devel()
