pkgname = "sslscan"
pkgver = "2.2.2"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"GIT_VERSION={pkgver}"]
makedepends = ["openssl3-devel"]
pkgdesc = "List supported ciphers in TLS servers"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f6095c01163eef04ff9b3540913f20d899f54e27b1194afd409c5fc807eacb46"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
