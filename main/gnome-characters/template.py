pkgname = "gnome-characters"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext-tiny",
    "itstool",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "glib-devel",
    "libunistring-devel",
    "gjs-devel",
]
depends = ["gnome-desktop", "gjs", "libadwaita"]
pkgdesc = "GNOME character map utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Design/Apps/CharacterMap"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "05b15c028cc190aef92e6092fd84fa8d5f2448e0e9076446a3566f3a081ff50b"
