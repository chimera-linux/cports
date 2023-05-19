pkgname = "lcms2"
pkgver = "2.15"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libtiff-devel"]
pkgdesc = "Small-footprint color management engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://littlecms.com"
source = f"https://github.com/mm2/Little-CMS/releases/download/lcms{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b20cbcbd0f503433be2a4e81462106fa61050a35074dc24a4e356792d971ab39"
# FIXME cfi
hardening = ["vis", "!cfi"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("lcms2-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()

@subpackage("lcms2-progs")
def _progs(self):
    return self.default_progs()

configure_gen = []
