pkgname = "gnome-calendar"
pkgver = "47.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calendar"
source = (
    f"$(GNOME_SITE)/gnome-calendar/{pkgver[:-2]}/gnome-calendar-{pkgver}.tar.xz"
)
sha256 = "3b03313f1c4d12dc821e07e209d1596d53eafa255d492d2ce5abf92ed1b51e76"
# FIXME
hardening = ["!int"]
