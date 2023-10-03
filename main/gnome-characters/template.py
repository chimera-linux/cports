pkgname = "gnome-characters"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
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
checkdepends = ["weston"]
depends = ["gnome-desktop", "gjs", "libadwaita"]
pkgdesc = "GNOME character map utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Design/Apps/CharacterMap"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3fd54fcc14d291b77fff12deefff00da383e0a6400af507d1605fbcb49b8c741"
