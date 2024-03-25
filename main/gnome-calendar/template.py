pkgname = "gnome-calendar"
pkgver = "46.0"
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
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME calendar"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calendar"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5e21960c174bd8606d9089bf79c70f31070ab4837919878b00db2f14af9fe718"
# FIXME
hardening = ["!int"]
