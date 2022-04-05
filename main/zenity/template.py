pkgname = "zenity"
pkgver = "3.42.0"
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
sha256 = "c24c7fe6bb43163ced8adf232d583b2e013d3ba6c28deb5fcf807985e3deb5ef"
