pkgname = "font-alias"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-fontrootdir=/usr/share/fonts"]
pkgdesc = "Standard aliases for X11 PCF fonts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/font/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f3111ae8bf2e980f5f56af400e8eefe5fc9f4207f4a412ea79637fd66c945276"

def post_install(self):
    self.install_license("COPYING")

# FIXME visibility
hardening = ["!vis"]
