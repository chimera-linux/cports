pkgname = "zenity"
pkgver = "4.2.2"
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
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libnotify-devel",
    "libx11-devel",
    "webkitgtk4-devel",
]
pkgdesc = "Display Gtk+ dialogs from the command line"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Zenity"
source = f"$(GNOME_SITE)/zenity/{pkgver[:-2]}/zenity-{pkgver}.tar.xz"
sha256 = "019186a996096ef4fc356e21577b5673f5baa3a29ac8e3d608b753371c18018d"
