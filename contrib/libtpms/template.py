pkgname = "libtpms"
pkgver = "0.9.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["openssl-devel"]
checkdepends = ["bash"]
pkgdesc = "Software emulation of a Trusted Platform Module"
maintainer = "cesorious <cesorious@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/stefanberger/libtpms"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2807466f1563ebe45fdd12dd26e501e8a0c4fbb99c7c428fbb508789efd221c0"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libtpms-devel")
def _(self):
    return self.default_devel()
