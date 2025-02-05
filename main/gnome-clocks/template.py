pkgname = "gnome-clocks"
pkgver = "47.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Clocks"
source = (
    f"$(GNOME_SITE)/gnome-clocks/{pkgver[:-2]}/gnome-clocks-{pkgver}.tar.xz"
)
sha256 = "428bdf4bd17e26de6cef014cd7a7eebd89143c3f2732b24b7da69812baa52131"
