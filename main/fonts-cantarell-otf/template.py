pkgname = "fonts-cantarell-otf"
pkgver = "0.303.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dfontsdir=/usr/share/fonts/cantarell",
    "-Duseprebuilt=true",
    "-Dbuildappstream=false",
]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Cantarell family of fonts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OFL-1.1"
url = "https://wiki.gnome.org/Projects/CantarellFonts"
source = f"$(GNOME_SITE)/cantarell-fonts/{pkgver[:-2]}/cantarell-fonts-{pkgver}.tar.xz"
sha256 = "f9463a0659c63e57e381fdd753cf1929225395c5b49135989424761830530411"


def post_install(self):
    self.install_license("COPYING")
