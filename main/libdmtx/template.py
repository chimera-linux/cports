pkgname = "libdmtx"
pkgver = "0.7.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
pkgdesc = "Data Matrix 2D library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/dmtx/libdmtx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7aa62adcefdd6e24bdabeb82b3ce41a8d35f4a0c95ab0c4438206aecafd6e1a1"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libdmtx-devel")
def _(self):
    return self.default_devel()
