pkgname = "zenity"
pkgver = "3.44.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny", "itstool"]
makedepends = [
    "gtk+3-devel",
    "glib-devel",
    "libnotify-devel",
    "libx11-devel",
    "webkitgtk-devel",
]
pkgdesc = "Display Gtk+ dialogs from the command line"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Zenity"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3fb5b8b1044d3d129262d3c54cf220eb7f76bc21bd5ac6d96ec115cd3518300e"
