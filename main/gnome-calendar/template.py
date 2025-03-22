pkgname = "gnome-calendar"
pkgver = "48.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
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
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calendar"
source = (
    f"$(GNOME_SITE)/gnome-calendar/{pkgver[:-2]}/gnome-calendar-{pkgver}.tar.xz"
)
sha256 = "06ceadd5c00be8e358181d421ecf2682ce0aea2fcb12d903b30d29ca33289f02"
# FIXME
hardening = ["!int"]
