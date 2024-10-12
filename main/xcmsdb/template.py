pkgname = "xcmsdb"
pkgver = "1.0.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
pkgdesc = "Device Color Characterization utility for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xcmsdb-{pkgver}.tar.gz"
sha256 = "2de6f66e1a25b7f6cbfb8f86b0e8da3fab454fc53a71b55a7705caf1a9d5677c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
