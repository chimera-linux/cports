pkgname = "libretls"
pkgver = "3.8.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = [
    "autoconf",
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "openssl-devel",
]
pkgdesc = "OpenSSL-based libtls implementation"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://git.causal.agency/libretls"
source = f"{url}/snapshot/{pkgname}-{pkgver}.tar.gz"
sha256 = "4a705c9c079dc70383ccc08432b93fbb61f9ec5873a92883e01e0940b8eaf3de"
# vis breaks symbols
hardening = []
# no tests
# header licence only
options = ["!check", "!distlicense"]


@subpackage("libretls-devel")
def _devel(self):
    return self.default_devel()
