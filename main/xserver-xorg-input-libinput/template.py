pkgname = "xserver-xorg-input-libinput"
pkgver = "1.4.0"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["xserver-xorg-devel", "libinput-devel"]
depends = ["virtual:xserver-abi-input~24!xserver-xorg-core"]
pkgdesc = "Generic input driver for X.org server based on libinput"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-input-libinput-{pkgver}.tar.gz"
sha256 = "e49131746f6fc639f58ee014b424a90be2e2073b55b9392517505fd3302fbbbe"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xorg-input-libinput-devel")
def _(self):
    return self.default_devel()
