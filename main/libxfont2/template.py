pkgname = "libxfont2"
pkgver = "2.0.6"
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
source = f"$(XORG_SITE)/lib/libXfont2-{pkgver}.tar.gz"
sha256 = "a944df7b6837c8fa2067f6a5fc25d89b0acc4011cd0bc085106a03557fb502fc"
# FIXME int (e.g. xorg fails check)
hardening = ["!int"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxfont2-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
