pkgname = "sslscan"
pkgver = "2.1.4"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"GIT_VERSION={pkgver}"]
makedepends = ["openssl-devel"]
pkgdesc = "List supported ciphers in TLS servers"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3e2a5b1f53d1f132b4d999ff450d2cc40e9efb648cea89b74f5944b768a10e63"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
