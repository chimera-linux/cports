pkgname = "libsrtp"
pkgver = "2.5.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcrypto-library=openssl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "Library for Secure Real-Time Transport Protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/cisco/libsrtp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8a43ef8e9ae2b665292591af62aa1a4ae41e468b6d98d8258f91478735da4e09"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsrtp-devel")
def _devel(self):
    return self.default_devel()
