pkgname = "font-alias"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-fontrootdir=/usr/share/fonts"]
# cycle with font-util
configure_gen = []
pkgdesc = "Standard aliases for X11 PCF fonts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/font-alias-{pkgver}.tar.gz"
sha256 = "f8e0ca6537003f11fcaf36c598f7de9c0428f8ed587388a8a37ff18ccc597730"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
