pkgname = "libsrtp"
pkgver = "2.4.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcrypto-library=openssl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = f"Library for Secure Real-Time Transport Protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/cisco/libsrtp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3b1bcb14ebda572b04b9bdf07574a449c84cb924905414e4d94e62837d22b628"
# unmarked api
hardening = ["!vis"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libsrtp-devel")
def _devel(self):
    return self.default_devel()
