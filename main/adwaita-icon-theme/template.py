pkgname = "adwaita-icon-theme"
pkgver = "49.0"
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
sha256 = "0702ce73eb9316d48f074b183ba71d87e9f9f76a399020de70f3eea824db8b5e"
