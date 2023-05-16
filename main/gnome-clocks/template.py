pkgname = "gnome-clocks"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool",
    "gobject-introspection", "gtk-update-icon-cache", "desktop-file-utils",
]
makedepends = [
    "gtk4-devel", "glib-devel", "gnome-desktop-devel", "libadwaita-devel",
    "libnotify-devel", "gsound-devel", "libgweather-devel", "geoclue-devel",
    "geocode-glib-devel",
]
depends = ["gsettings-desktop-schemas", "desktop-file-utils"]
pkgdesc = "GNOME clock application"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Clocks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "17d7a97365cb8f1a023a1d78f7501f3353217fa7577d73afe7d0ca1e3b4f3838"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
