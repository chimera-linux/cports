pkgname = "mkfontscale"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-bzip2"]
hostmakedepends = ["pkgconf"]
makedepends = [
    "xorgproto",
    "zlib-devel",
    "libbz2-devel",
    "freetype-devel",
    "libfontenc-devel",
]
triggers = ["/usr/share/fonts/*"]
pkgdesc = "X11 scalable font index generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/app/{pkgname}-{pkgver}.tar.gz"
sha256 = "4a5af55e670713024639a7f7d10826d905d86faf574cd77e0f5aef2d00e70168"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
