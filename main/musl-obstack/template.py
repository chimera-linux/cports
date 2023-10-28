pkgname = "musl-obstack"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./bootstrap.sh"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Implementation of obstack for musl"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/void-linux/musl-obstack"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9ffb3479b15df0170eba4480e51723c3961dbe0b461ec289744622db03a69395"


@subpackage("musl-obstack-devel")
def _devel(self):
    return self.default_devel()
