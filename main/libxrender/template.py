pkgname = "libxrender"
pkgver = "0.9.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "X Render library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXrender-{pkgver}.tar.gz"
sha256 = "6aec3ca02e4273a8cbabf811ff22106f641438eb194a12c0ae93c7e08474b667"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxrender-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
