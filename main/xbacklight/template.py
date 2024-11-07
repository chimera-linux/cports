pkgname = "xbacklight"
pkgver = "1.2.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel", "libxrandr-devel", "xcb-util-devel"]
pkgdesc = "Adjusts X backlight brightness"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xbacklight-{pkgver}.tar.xz"
sha256 = "d4c30b0e6f18c82f387585a737ee3b72d468c927892b08a898c41bc12248e8ee"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
