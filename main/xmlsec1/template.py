pkgname = "xmlsec1"
pkgver = "1.3.12"
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
license = "MIT"
url = "https://www.aleksey.com/xmlsec"
source = f"{url}/download/xmlsec1-{pkgver}.tar.gz"
sha256 = "24045199af12d93fe5fdbbbf7e386e823e4842071e9432e2b90ac108b889a923"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _(self):
    return self.default_devel()
