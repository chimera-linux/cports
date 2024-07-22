pkgname = "xinput"
pkgver = "1.6.4"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "libxext-devel",
    "libxi-devel",
    "libxrandr-devel",
    "libxinerama-devel",
]
pkgdesc = "X input device configuration utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xinput-{pkgver}.tar.gz"
sha256 = "64e25434af1309ed0abca1ebebd035f7631bb0bc1bfac5decefe9aa98ccaf611"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
