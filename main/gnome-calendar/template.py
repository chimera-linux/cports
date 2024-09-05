pkgname = "gnome-calendar"
pkgver = "47_rc"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "evolution-data-server-devel",
    "geoclue-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libical-devel",
    "libsoup-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME calendar"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calendar"
source = f"$(GNOME_SITE)/gnome-calendar/{pkgver[:2]}/gnome-calendar-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "736901c04fe50957fda2c85e52c6b6be2e3b0838188bc138492dea788c2e7d60"
# FIXME
hardening = ["!int"]
