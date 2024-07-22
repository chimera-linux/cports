pkgname = "xbacklight"
pkgver = "1.2.3"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxrandr-devel", "xcb-util-devel"]
pkgdesc = "Adjusts X backlight brightness"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xbacklight-{pkgver}.tar.bz2"
sha256 = "3a27f324777ae99fee476cfb2f064576fb8cba4eb77f97cda37adda1c1d39ade"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
