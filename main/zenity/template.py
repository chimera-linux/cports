pkgname = "zenity"
pkgver = "4.0.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwebkitgtk=true"]
hostmakedepends = [
    "gettext",
    "help2man",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libadwaita-devel",
    "libnotify-devel",
    "libx11-devel",
    "webkitgtk4-devel",
]
pkgdesc = "Display Gtk+ dialogs from the command line"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Zenity"
source = f"$(GNOME_SITE)/zenity/{pkgver[:-2]}/zenity-{pkgver}.tar.xz"
sha256 = "b429d97b87bd9ce7fb72ac0b78df534725d8ad39817ddca6a4ca2ee5381b08de"
