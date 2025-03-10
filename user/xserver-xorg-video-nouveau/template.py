pkgname = "xserver-xorg-video-nouveau"
pkgver = "1.0.18"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "libdrm-devel",
    "libpciaccess-devel",
    "udev-devel",
    "xserver-xorg-devel",
]
pkgdesc = "NVIDIA Nouveau video driver"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-video-nouveau-{pkgver}.tar.gz"
sha256 = "b916f3174bed1df6e3ab8998053172ffabc563f86279bb7abb27b6b699ac556f"
tool_flags = {"LDFLAGS": ["-Wl,-z,lazy"]}
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")
