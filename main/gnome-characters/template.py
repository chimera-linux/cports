pkgname = "gnome-characters"
pkgver = "47_alpha"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gtk-update-icon-cache",
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
source = f"$(GNOME_SITE)/gnome-characters/{pkgver[:2]}/gnome-characters-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "fa6adadcc7f09221bd8dcc59e60eb917ec6c120e4d2333d0e75389e53b5d6af2"
