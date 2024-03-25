pkgname = "gnome-clocks"
pkgver = "46.0"
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
    "gtk-update-icon-cache",
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "eaa3c578cdcef9754e668b5626709b73f3526710235f4b72076d2ff49a4f99c7"
