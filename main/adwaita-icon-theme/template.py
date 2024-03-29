pkgname = "adwaita-icon-theme"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
depends = ["hicolor-icon-theme"]
pkgdesc = "Icon theme for GTK+"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later OR CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/adwaita-icon-theme"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4bcb539bd75d64da385d6fa08cbaa9ddeaceb6ac8e82b85ba6c41117bf5ba64e"
