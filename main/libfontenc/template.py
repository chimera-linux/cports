pkgname = "libfontenc"
pkgver = "1.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-encodingsdir=/usr/share/fonts/encodings"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "zlib-devel"]
pkgdesc = "Fontenc Library from X.org"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.gz"
sha256 = "c103543a47ce5c0200fb1867f32df5e754a7c3ef575bf1fe72187117eac22a53"
# unmarked api
hardening = ["!vis"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libfontenc-devel")
def _devel(self):
    return self.default_devel()
