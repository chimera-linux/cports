pkgname = "libatomic_ops"
pkgver = "7.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static", "--enable-shared"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Library for atomic operations"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND GPL-2.0-or-later"
url = "https://github.com/ivmai/libatomic_ops"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "15676e7674e11bda5a7e50a73f4d9e7d60452271b8acf6fd39a71fefdf89fa31"


@subpackage("libatomic_ops-devel")
def _devel(self):
    return self.default_devel()
