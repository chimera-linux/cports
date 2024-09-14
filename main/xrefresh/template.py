pkgname = "xrefresh"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = ["libx11-devel"]
pkgdesc = "Refresh all or a part of an X screen"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xrefresh-{pkgver}.tar.gz"
sha256 = "cbf0d3ed80f03188841a96ceb20e615b40a006e3928be2e179d9d5a0ded639b2"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
