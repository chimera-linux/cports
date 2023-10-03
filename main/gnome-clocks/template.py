pkgname = "gnome-clocks"
pkgver = "45.0"
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
depends = ["gsettings-desktop-schemas", "desktop-file-utils"]
pkgdesc = "GNOME clock application"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Clocks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fc8eb4fd9530f1e641dc00ee2086ee7d354a7a00b0a0d1722e305d5c9aab91b5"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
