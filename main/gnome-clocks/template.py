pkgname = "gnome-clocks"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "ffmpeg",
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
sha256 = "4bdf9c0481a83037da1d0fa26d2c2c6a80cb736458fd18fde14acaf7924874c6"
