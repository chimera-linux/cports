pkgname = "zenity"
pkgver = "4.2.0"
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
sha256 = "5f983340c6fa55f4fab5a9769d0771b2cdf1365e2c158ac11cc16ffd892f6bcd"
