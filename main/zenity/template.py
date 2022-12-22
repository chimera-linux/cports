pkgname = "zenity"
pkgver = "3.43.0"
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
sha256 = "b0d7ca1e0c1868fa18f05c210260d8a7be1f08ee13b7f5cfdbab9b61fa16f833"

# FIXME visibility
hardening = ["!vis"]
