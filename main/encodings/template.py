pkgname = "encodings"
pkgver = "1.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-encodingsdir=/usr/share/fonts/encodings",
]
hostmakedepends = [
    "automake",
    "font-util-devel",
    "mkfontscale",
    "pkgconf",
    "xorg-util-macros",
]
pkgdesc = "Font encoding tables for libfontenc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/encodings-{pkgver}.tar.gz"
sha256 = "7d9b7afedc97c3b29b6262b3346728b877f0a91a4a5802bf091df4cffb43a568"


def post_install(self):
    self.install_license("COPYING")
