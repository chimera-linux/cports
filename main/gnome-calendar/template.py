pkgname = "gnome-calendar"
pkgver = "49.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
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
    f"$(GNOME_SITE)/gnome-calendar/{pkgver[:-4]}/gnome-calendar-{pkgver}.tar.xz"
)
sha256 = "e0bfe4ea109422dada0745dd8f8c0e0230ab88207710d1c07e245322cf913ff2"
# FIXME
hardening = ["!int"]
