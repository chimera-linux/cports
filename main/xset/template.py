pkgname = "xset"
pkgver = "1.2.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = [
    "libxext-devel",
    "libxfontcache-devel",
    "libxmu-devel",
    "libxxf86misc-devel",
]
pkgdesc = "X11 user preferences utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xset-{pkgver}.tar.gz"
sha256 = "2068d1356d80c29ce283f0fff5895667b38f24ea95df363d3dde7b8c8a92fffe"
hardening = ["vis", "cfi"]
# needs cmdtest
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
