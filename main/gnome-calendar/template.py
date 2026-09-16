pkgname = "gnome-calendar"
pkgver = "51.0"
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
    f"$(GNOME_SITE)/gnome-calendar/{pkgver[:2]}/gnome-calendar-{pkgver}.tar.xz"
)
sha256 = "77c290450c40834392cdea2c40451561e98f43d5dae93cd9e915051a6708dc30"
# FIXME
hardening = ["!int"]
