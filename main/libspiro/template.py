pkgname = "libspiro"
pkgver = "20200505"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Simplifies the drawing of beautiful curves"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/fontforge/libspiro"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "00be530b5c0ea9274baadf6c05521f0b192d4c3c1db636ac8b08efd44aaea8f5"

def pre_configure(self):
    self.do("autoreconf", "-if")

@subpackage("libspiro-static")
def _static(self):
    return self.default_static()

@subpackage("libspiro-devel")
def _devel(self):
    return self.default_devel(man = True)
