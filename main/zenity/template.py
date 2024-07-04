pkgname = "zenity"
pkgver = "4.0.2"
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
sha256 = "c16dcae46e29e22c2fa0b95e80e06c96b2aec93840161369c95c85ed9f093153"
