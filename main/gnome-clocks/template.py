pkgname = "gnome-clocks"
pkgver = "50.0"
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
sha256 = "bf167f7f44f4f2fb424d4716652c9ba1f29e16e49071e26a1bb833f8dce794c6"
