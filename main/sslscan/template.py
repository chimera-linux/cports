pkgname = "sslscan"
pkgver = "2.1.6"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"GIT_VERSION={pkgver}"]
makedepends = ["openssl3-devel"]
pkgdesc = "List supported ciphers in TLS servers"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later WITH custom:OpenSSL-exception"
url = "https://github.com/rbsec/sslscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5995b32c065715e8da2fd83ad99c07de4938ff55d46c6665bdc71b74814236a8"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
