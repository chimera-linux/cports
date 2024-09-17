pkgname = "sslscan"
pkgver = "2.1.5"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"GIT_VERSION={pkgver}"]
makedepends = ["openssl-devel"]
pkgdesc = "List supported ciphers in TLS servers"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f1fa33deba4033745cdfda5d0674f4f6e9f572548062737acc04b3e972edc43f"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
