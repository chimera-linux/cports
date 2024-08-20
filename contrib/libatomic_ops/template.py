pkgname = "libatomic_ops"
pkgver = "7.8.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static", "--enable-shared"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library for atomic operations"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND GPL-2.0-or-later"
url = "https://github.com/ivmai/libatomic_ops"
source = f"{url}/releases/download/v{pkgver}/libatomic_ops-{pkgver}.tar.gz"
sha256 = "d305207fe207f2b3fb5cb4c019da12b44ce3fcbc593dfd5080d867b1a2419b51"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libatomic_ops-devel")
def _(self):
    return self.default_devel()
