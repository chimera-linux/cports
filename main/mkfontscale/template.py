pkgname = "mkfontscale"
pkgver = "1.2.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-bzip2"]
hostmakedepends = ["automake", "pkgconf", "xorg-util-macros"]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "libfontenc-devel",
    "xorgproto",
    "zlib-devel",
]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "X11 scalable font index generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "3a026b468874eb672a1d0a57dbd3ddeda4f0df09886caf97d30097b70c2df3f8"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
