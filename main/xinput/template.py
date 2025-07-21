pkgname = "xinput"
pkgver = "1.6.4"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "libxext-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxrandr-devel",
]
pkgdesc = "X input device configuration utility"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xinput-{pkgver}.tar.gz"
sha256 = "64e25434af1309ed0abca1ebebd035f7631bb0bc1bfac5decefe9aa98ccaf611"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
