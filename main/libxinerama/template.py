pkgname = "libxinerama"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "PanoramiX extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXinerama-{pkgver}.tar.bz2"
sha256 = "0008dbd7ecf717e1e507eed1856ab0d9cf946d03201b85d5dcf61489bb02d720"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxinerama-devel")
def _devel(self):
    return self.default_devel()
