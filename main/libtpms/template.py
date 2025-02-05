pkgname = "libtpms"
pkgver = "0.10.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["openssl3-devel"]
checkdepends = ["bash"]
pkgdesc = "Software emulation of a Trusted Platform Module"
maintainer = "cesorious <cesorious@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/stefanberger/libtpms"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6da9a527b3afa7b1470acd4cd17157b8646c31a2c7ff3ba2dfc50c81ba413426"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libtpms-devel")
def _(self):
    return self.default_devel()
