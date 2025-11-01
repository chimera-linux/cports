pkgname = "gnome-characters"
pkgver = "49.1"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gjs-devel",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libunistring-devel",
]
checkdepends = ["fonts-dejavu", "xwayland-run"]
depends = ["gjs", "gnome-desktop", "libadwaita"]
pkgdesc = "GNOME character map utility"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Design/Apps/CharacterMap"
source = f"$(GNOME_SITE)/gnome-characters/{pkgver[:-2]}/gnome-characters-{pkgver}.tar.xz"
sha256 = "795c0fe434e602dc783391fb5830dbc7d8e1ea05ca77210fb140e2f6f40a145c"
# tries to access gpu
options = ["!check"]
