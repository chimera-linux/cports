pkgname = "libxfontcache"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X-TrueType font cache extension client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXfontcache-{pkgver}.tar.bz2"
sha256 = "0d639219549f51fa0e6b4414383f5d13e6c1638e66b3434f4626eb989ffacbce"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxfontcache-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
