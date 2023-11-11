pkgname = "gnome-calendar"
pkgver = "45.1"
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
sha256 = "7fa8507543865aa7432bb5319830c87158b5447ca09cca45b607dc6796c71008"
# FIXME
hardening = ["!int"]
