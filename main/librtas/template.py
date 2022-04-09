pkgname = "librtas"
pkgver = "2.0.3"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Librtas library for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ibm-power-utilities/librtas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1b951422ec9553fa9d5e5e158fd8e298f867f561189fff6817a9540d5661f145"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

@subpackage("librtas-devel")
def _devel(self):
    return self.default_devel()
