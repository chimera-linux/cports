pkgname = "xdpyinfo"
pkgver = "1.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-dmx"]
hostmakedepends = ["pkgconf", "automake", "libtool", "xorg-util-macros"]
makedepends = [
    "libxcomposite-devel",
    "libxext-devel",
    "libxinerama-devel",
    "libxrender-devel",
    "libxtst-devel",
    "libxxf86misc-devel",
    "libxxf86vm-devel",
]
pkgdesc = "X display information utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xdpyinfo-{pkgver}.tar.gz"
sha256 = "bbbe0b75935285fbb4c795b4f1d3d4f9c91cd4c18f4b6fd7107c648094172f7b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
