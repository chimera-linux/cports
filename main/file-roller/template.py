pkgname = "file-roller"
pkgver = "44"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "glib-devel",
    "desktop-file-utils",
    "itstool",
    "gtk-update-icon-cache",
]
makedepends = [
    "gtk4-devel",
    "glib-devel",
    "libarchive-devel",
    "libnotify-devel",
    "nautilus-devel",
    "libadwaita-devel",
    "libportal-devel",
    "json-glib-devel",
]
pkgdesc = "GNOME archiver frontend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/FileRoller"
source = f"https://gitlab.gnome.org/GNOME/file-roller/-/archive/{pkgver}/file-roller-{pkgver}.tar.gz"
sha256 = "2f72870d6af05b044f37ef0a09aa105852c26d606a9cf68cd6a6fdb3f9ee7e87"
