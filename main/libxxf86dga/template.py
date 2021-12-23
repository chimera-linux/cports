pkgname = "libxxf86dga"
pkgver = "1.1.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "XFree86-DGA X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86dga-{pkgver}.tar.bz2"
sha256 = "2b98bc5f506c6140d4eddd3990842d30f5dae733b64f198a504f07461bdb7203"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxxf86dga-static")
def _static(self):
    return self.default_static()

@subpackage("libxxf86dga-devel")
def _devel(self):
    return self.default_devel()
