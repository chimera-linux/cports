pkgname = "gnome-clocks"
pkgver = "48.0"
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
sha256 = "616ee1fb75300b1f26b9766219e954751360ca0fa0f491311bcf83bf38087c62"
