pkgname = "libsrtp"
pkgver = "2.8.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dcrypto-library=openssl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Library for Secure Real-Time Transport Protocol"
license = "BSD-3-Clause"
url = "https://github.com/cisco/libsrtp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ef5569220749529d778013aae1178391d972570a2b4f7288dda22effa875b07c"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsrtp-devel")
def _(self):
    return self.default_devel()
