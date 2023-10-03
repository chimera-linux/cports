pkgname = "gnome-calendar"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "itstool",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "evolution-data-server-devel",
    "gsettings-desktop-schemas-devel",
    "libgweather-devel",
    "libical-devel",
    "geoclue-devel",
    "libpeas-devel",
    "libsoup-devel",
]
depends = ["gsettings-desktop-schemas", "desktop-file-utils"]
pkgdesc = "GNOME calendar"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calendar"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8c1483cbba4388db410875ed09d64e9003f929b555d704076a6fe7bd7c1e65b2"
# FIXME
hardening = ["!int"]
