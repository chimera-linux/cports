pkgname = "adwaita-icon-theme"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
depends = ["hicolor-icon-theme"]
pkgdesc = "Icon theme for GTK+"
license = "LGPL-3.0-or-later OR CC-BY-SA-3.0"
url = "https://gitlab.gnome.org/GNOME/adwaita-icon-theme"
# missing tarball
# source = f"$(GNOME_SITE)/adwaita-icon-theme/{pkgver[:-2]}/adwaita-icon-theme-{pkgver}.tar.xz"
source = f"https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/archive/{pkgver}/adwaita-icon-theme-{pkgver}.tar.gz"
sha256 = "403f650189cc41ba8321417470cbb7e484425374df7a52a3289421b9ac30e792"
