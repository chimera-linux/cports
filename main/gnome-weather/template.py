pkgname = "gnome-weather"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
    "typescript",
]
makedepends = [
    "geoclue-devel",
    "gjs-devel",
    "gobject-introspection-devel",
    "libadwaita-devel",
    "libgweather-devel",
]
depends = ["geoclue", "gjs", "libadwaita", "libgweather"]
pkgdesc = "GNOME weather application"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Weather"
source = (
    f"$(GNOME_SITE)/gnome-weather/{pkgver[:-2]}/gnome-weather-{pkgver}.tar.xz"
)
sha256 = "57de7578605f91f9ab400551ce7738db7505bc88f42a33c70ce7a70167fdb513"
