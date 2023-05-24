pkgname = "adwaita-icon-theme"
pkgver = "44.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Icon theme for GTK+"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later OR CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/adwaita-icon-theme"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4889c5601bbfecd25d80ba342209d0a936dcf691ee56bd6eca4cde361f1a664c"

configure_gen = []
