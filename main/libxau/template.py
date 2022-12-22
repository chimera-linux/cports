pkgname = "libxau"
pkgver = "1.0.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto"]
pkgdesc = "Authorization Protocol for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXau-{pkgver}.tar.gz"
sha256 = "51a54da42475d4572a0b59979ec107c27dacf6c687c2b7b04e5cf989a7c7e60c"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxau-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
