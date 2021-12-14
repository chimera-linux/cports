pkgname = "libxfont2"
pkgver = "2.0.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto", "xtrans", "freetype-devel", "libfontenc-devel"
]
pkgdesc = "X font 2 library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXfont2-{pkgver}.tar.bz2"
sha256 = "aa7c6f211cf7215c0ab4819ed893dc98034363d7b930b844bb43603c2e10b53e"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxfont2-static")
def _static(self):
    return self.default_static()

@subpackage("libxfont2-devel")
def _devel(self):
    return self.default_devel(man = True)
