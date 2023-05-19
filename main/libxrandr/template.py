pkgname = "libxrandr"
pkgver = "1.5.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel", "libxrender-devel"]
pkgdesc = "X RandR Library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrandr-{pkgver}.tar.gz"
sha256 = "3ad316c1781fe2fe22574b819e81f0eff087a8560377f521ba932238b41b251f"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxrandr-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
