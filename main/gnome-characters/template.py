pkgname = "gnome-characters"
pkgver = "46.0"
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
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a4e8e2c510bf48204b9994a4e7cd537844246e74c8a986f9dbe04e223f5d827c"
