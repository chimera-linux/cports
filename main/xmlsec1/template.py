pkgname = "xmlsec1"
pkgver = "1.3.7"
pkgrel = 1
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
sha256 = "d82e93b69b8aa205a616b62917a269322bf63a3eaafb3775014e61752b2013ea"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("xmlsec1-devel")
def _(self):
    return self.default_devel()
