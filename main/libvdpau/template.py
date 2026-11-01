pkgname = "libvdpau"
pkgver = "1.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libxext-devel", "xorgproto"]
pkgdesc = "Video Decode and Presentation API for UNIX"
license = "MIT"
url = "https://freedesktop.org/wiki/Software/VDPAU"
source = f"https://gitlab.freedesktop.org/vdpau/libvdpau/-/archive/{pkgver}/libvdpau-{pkgver}.tar.gz"
sha256 = "66490802f30426d30ff9e8af35263bbbbaa23b52d0a2d797d06959c3d19638fd"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libvdpau-devel")
def _(self):
    self.depends += ["libx11-devel"]
    return self.default_devel()
