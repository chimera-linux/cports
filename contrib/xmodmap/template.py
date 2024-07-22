pkgname = "xmodmap"
pkgver = "1.0.11"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libx11-devel"]
pkgdesc = "Modify X keymaps and pointer button mappings"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/xmodmap-{pkgver}.tar.gz"
sha256 = "c4fac9df448b98ac5a1620f364e74ed5f7084baae0d09123700f34d4b63cb5d8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
