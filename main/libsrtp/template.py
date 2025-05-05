pkgname = "libsrtp"
pkgver = "2.7.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcrypto-library=openssl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Library for Secure Real-Time Transport Protocol"
license = "BSD-3-Clause"
url = "https://github.com/cisco/libsrtp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "54facb1727a557c2a76b91194dcb2d0a453aaf8e2d0cbbf1e3c2848c323e28ad"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsrtp-devel")
def _(self):
    return self.default_devel()
