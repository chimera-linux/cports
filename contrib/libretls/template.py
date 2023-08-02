pkgname = "libretls"
pkgver = "3.7.0"
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
sha256 = "cd72a37e93f8376c2e6310d30d39cda3d0f358bf3763d3ff22faf2454c3b25ed"
# vis breaks symbols
hardening = []
# no tests
# header licence only
options = ["!check", "!distlicense"]


@subpackage("libretls-devel")
def _devel(self):
    return self.default_devel()
