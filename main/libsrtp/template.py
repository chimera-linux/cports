pkgname = "libsrtp"
pkgver = "2.8.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcrypto-library=openssl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Library for Secure Real-Time Transport Protocol"
license = "BSD-3-Clause"
url = "https://github.com/cisco/libsrtp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d123dcff5c56d4f1a9006f2b311ea99a85016cbf3bb24b1007885d422237db85"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsrtp-devel")
def _(self):
    return self.default_devel()
