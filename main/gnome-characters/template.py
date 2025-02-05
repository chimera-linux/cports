pkgname = "gnome-characters"
pkgver = "47.0"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Design/Apps/CharacterMap"
source = f"$(GNOME_SITE)/gnome-characters/{pkgver[:-2]}/gnome-characters-{pkgver}.tar.xz"
sha256 = "6bcf05a22f30f131d8a8035b0f63d86a9567007a5f6df5ce8556ba06777b7574"
