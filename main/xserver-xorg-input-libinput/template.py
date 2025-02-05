pkgname = "xserver-xorg-input-libinput"
pkgver = "1.5.0"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = ["xserver-xorg-devel", "libinput-devel"]
depends = ["virtual:xserver-abi-input~24!xserver-xorg-core"]
provides = [self.with_pkgver("xserver-xorg-input-driver")]
pkgdesc = "Generic input driver for X.org server based on libinput"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/driver/xf86-input-libinput-{pkgver}.tar.gz"
sha256 = "936ce0ad647b49eb332c7d72945e346ffc61d48a45a009e3f0403a90dbf5908e"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xorg-input-libinput-devel")
def _(self):
    return self.default_devel()
