pkgname = "libxtst"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel", "libxi-devel"]
pkgdesc = "X Tst library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXtst-{pkgver}.tar.gz"
sha256 = "01366506aeb033f6dffca5326af85f670746b0cabbfd092aabefb046cf48c445"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxtst-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
