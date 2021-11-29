pkgname = "libxxf86vm"
pkgver = "1.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-malloc0returnsnull"]
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "libxext-devel"]
pkgdesc = "XFree86-VidMode X extension library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXxf86vm-{pkgver}.tar.bz2"
sha256 = "afee27f93c5f31c0ad582852c0fb36d50e4de7cd585fcf655e278a633d85cd57"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxxf86vm-static")
def _static(self):
    return self.default_static()

@subpackage("libxxf86vm-devel")
def _devel(self):
    return self.default_devel(extra = ["usr/share"])
