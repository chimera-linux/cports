pkgname = "gnome-clocks"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "itstool",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "libadwaita-devel",
    "libnotify-devel",
    "gsound-devel",
    "libgweather-devel",
    "geoclue-devel",
    "geocode-glib-devel",
]
depends = ["gsettings-desktop-schemas"]
pkgdesc = "GNOME clock application"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Clocks"
source = (
    f"$(GNOME_SITE)/gnome-clocks/{pkgver[:-2]}/gnome-clocks-{pkgver}.tar.xz"
)
sha256 = "616ee1fb75300b1f26b9766219e954751360ca0fa0f491311bcf83bf38087c62"
