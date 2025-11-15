pkgname = "xmlsec1"
pkgver = "1.3.9"
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
sha256 = "a631c8cd7a6b86e6adb9f5b935d45a9cf9768b3cb090d461e8eb9d043cf9b62f"
# broken tests build + tests reach internet
options = ["!cross", "!check"]


def post_install(self):
    self.install_license("COPYING")
    self.uninstall("usr/bin/xmlsec_unit_tests")


@subpackage("xmlsec1-devel")
def _(self):
    return self.default_devel()
