pkgname = "libdmtx"
pkgver = "0.7.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Data Matrix 2D library"
license = "BSD-2-Clause"
url = "https://github.com/dmtx/libdmtx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2394bf1d1d693a5a4ca3cfcc1bb28a4d878bdb831ea9ca8f3d5c995d274bdc39"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdmtx-devel")
def _(self):
    return self.default_devel()
