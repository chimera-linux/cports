pkgname = "sslscan"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"GIT_VERSION={pkgver}"]
makedepends = ["openssl3-devel"]
pkgdesc = "List supported ciphers in TLS servers"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "17c6fe4a7822e1949bc8975feea59fcf042c4a46d62d9f5acffe59afc466cc1c"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
