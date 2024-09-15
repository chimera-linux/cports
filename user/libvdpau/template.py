pkgname = "libvdpau"
pkgver = "1.5"
pkgrel = 0
archs = ["x86_64"]
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libx11-devel", "libxext-devel"]
pkgdesc = "VDPAU wrapper and trace libraries"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/VDPAU"
source = f"https://gitlab.freedesktop.org/vdpau/{pkgname}/-/archive/{pkgver}/{pkgver}.tar.bz2"
sha256 = "02055ce69154de39e2d0dc53d4ab5d96a6c2a06b2beaa82e52e86f43119730a4"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libvdpau-devel")
def _(self):
    return self.default_devel()
