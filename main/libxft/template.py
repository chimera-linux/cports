pkgname = "libxft"
pkgver = "2.3.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto", "libxrender-devel", "freetype-devel", "fontconfig-devel"
]
pkgdesc = "X font library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXft-{pkgver}.tar.gz"
sha256 = "75b4378644f5df3a15f684f8f0b5ff1324d37aacd5a381f3b830a2fbe985f660"
# crashes
hardening = ["!int"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxft-devel")
def _devel(self):
    return self.default_devel()
