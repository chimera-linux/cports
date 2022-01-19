pkgname = "zenity"
pkgver = "3.41.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny", "itstool"]
makedepends = [
    "gtk+3-devel", "libglib-devel", "libnotify-devel", "libx11-devel",
    "webkitgtk-devel"
]
pkgdesc = "Display Gtk+ dialogs from the command line"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Zenity"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "19b676c3510e22badfcc3204062d432ba537402f5e0ae26128c0d90c954037e1"
