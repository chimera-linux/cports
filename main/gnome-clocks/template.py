pkgname = "gnome-clocks"
pkgver = "49.0"
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
    "vala",
]
makedepends = [
    "geoclue-devel",
    "geocode-glib-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gsound-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libnotify-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME clock application"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Clocks"
source = (
    f"$(GNOME_SITE)/gnome-clocks/{pkgver[:-2]}/gnome-clocks-{pkgver}.tar.xz"
)
sha256 = "bf76915f2a492e8a0592fe40b35346593aa39e4e6881d6176e0efd8771d4e6fa"
