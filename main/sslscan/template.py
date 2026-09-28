pkgname = "sslscan"
pkgver = "2.2.3"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"GIT_VERSION={pkgver}"]
makedepends = ["openssl3-devel"]
pkgdesc = "List supported ciphers in TLS servers"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b0498467604c3f4eb7a1b3258ee9f37b709f7844d7edf338d40e85af40ede960"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
