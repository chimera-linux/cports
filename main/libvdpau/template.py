pkgname = "libvdpau"
pkgver = "1.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libxext-devel", "xorgproto"]
pkgdesc = "Video Decode and Presentation API for UNIX"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://freedesktop.org/wiki/Software/VDPAU"
source = f"https://gitlab.freedesktop.org/vdpau/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "66490802f30426d30ff9e8af35263bbbbaa23b52d0a2d797d06959c3d19638fd"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libvdpau-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
