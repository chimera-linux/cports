pkgname = "xwininfo"
pkgver = "1.1.6"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
pkgdesc = "Query information about X windows"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xwininfo-{pkgver}.tar.gz"
sha256 = "2d52151de9d2808343c715c480e7d37f88958c8b7fcd090178b097436d987c2b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
