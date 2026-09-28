pkgname = "xsetroot"
pkgver = "1.1.3"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = [
    "libxcursor-devel",
    "libxfixes-devel",
    "libxmu-devel",
    "libxrender-devel",
    "xbitmaps",
]
pkgdesc = "X root window parameter setting utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xsetroot-{pkgver}.tar.gz"
sha256 = "80dbb0d02807e89294a042298b8a62f9aa0c3a94d89244ccbc35e4cf80fcaaba"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
