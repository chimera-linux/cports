pkgname = "libxscrnsaver"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libx11-devel", "libxext-devel"]
pkgdesc = "X Screensaver Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXScrnSaver-{pkgver}.tar.bz2"
sha256 = "f917075a1b7b5a38d67a8b0238eaab14acd2557679835b154cf2bca576e89bf8"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxscrnsaver-devel")
def _devel(self):
    return self.default_devel()
