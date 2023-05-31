pkgname = "zenity"
pkgver = "3.44.1"
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
sha256 = "d65400aec965411f4c0b3d8e0e0dac54be55d807a29279697537da2dfee93eaa"
