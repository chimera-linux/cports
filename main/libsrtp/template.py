pkgname = "libsrtp"
pkgver = "2.6.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcrypto-library=openssl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Library for Secure Real-Time Transport Protocol"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/cisco/libsrtp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "bf641aa654861be10570bfc137d1441283822418e9757dc71ebb69a6cf84ea6b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsrtp-devel")
def _(self):
    return self.default_devel()
