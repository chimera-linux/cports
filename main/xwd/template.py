pkgname = "xwd"
pkgver = "1.0.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel", "libxkbfile-devel"]
pkgdesc = "Dump an image of an X window"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.bz2"
sha256 = "fbaa2b34163714fe7be22b60920ea4683f63b355babb1781aec2e452a033031b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
