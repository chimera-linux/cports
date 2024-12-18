pkgname = "xserver-xorg-video-ati"
pkgver = "22.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "libdrm-devel",
    "libpciaccess-devel",
    "mesa-devel",
    "pixman-devel",
    "udev-devel",
    "xserver-xorg-devel",
]
pkgdesc = "Xorg ATI Radeon video driver"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-video-ati-{pkgver}.tar.gz"
sha256 = "75f2d4ed4d1041ae9eb2a11816b919e18aee9a25db1556b3d938fff31d3c86f3"
tool_flags = {"LDFLAGS": ["-Wl,-z,lazy"]}
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")
