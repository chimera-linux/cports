pkgname = "sslscan"
pkgver = "2.1.3"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [f"GIT_VERSION={pkgver}"]
hostmakedepends = ["gmake"]
makedepends = ["openssl-devel"]
pkgdesc = "List supported ciphers in TLS servers"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6beec9345635b41fa2c1bbc5f0854f10014e4b2b4179e9e9a3bda6bdb9e1aa41"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
