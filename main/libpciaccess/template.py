pkgname = "libpciaccess"
pkgver = "0.17"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "X11 PCI access library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/{pkgname}-{pkgver}.tar.gz"
sha256 = "bf6985a77d2ecb00e2c79da3edfb26b909178ffca3f2e9d14ed0620259ab733b"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libpciaccess-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
