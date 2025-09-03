pkgname = "xserver-xorg-video-fbdev"
pkgver = "0.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["xserver-xorg-devel"]
pkgdesc = "Xorg framebuffer video driver"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-video-fbdev-{pkgver}.tar.gz"
sha256 = "5e73c01f6ede09ddbc1f553fecdf35dd8efe76b44c7ed263de786a5968c5116f"
tool_flags = {"LDFLAGS": ["-Wl,-z,lazy"]}
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")
