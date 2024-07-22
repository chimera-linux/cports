pkgname = "xcmsdb"
pkgver = "1.0.6"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Device Color Characterization utility for X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xcmsdb-{pkgver}.tar.gz"
sha256 = "640b42c746eb34bdd71ca2850f2bc9fb0ade194c9f152a8d002425a0684df077"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
