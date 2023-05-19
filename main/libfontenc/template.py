pkgname = "libfontenc"
pkgver = "1.1.7"
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
sha256 = "5e5f210329823f08f97bfe9fd5b4105070c789bc5aef88ce01d86d8203d4aa9f"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libfontenc-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
