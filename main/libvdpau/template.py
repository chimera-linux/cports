pkgname = "libvdpau"
pkgver = "1.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libxext-devel", "xorgproto"]
pkgdesc = "Video Decode and Presentation API for UNIX"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://freedesktop.org/wiki/Software/VDPAU"
source = f"https://gitlab.freedesktop.org/vdpau/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "240dd8f9ec08de707529917677827ba12e13b9fc299eeb3af13ea05e7fc74aba"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libvdpau-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
