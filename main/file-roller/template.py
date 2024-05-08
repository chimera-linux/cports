pkgname = "file-roller"
pkgver = "44.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libarchive-devel",
    "libnotify-devel",
    "libportal-devel",
    "nautilus-devel",
]
pkgdesc = "GNOME archiver frontend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/FileRoller"
source = f"https://gitlab.gnome.org/GNOME/file-roller/-/archive/{pkgver}/file-roller-{pkgver}.tar.gz"
sha256 = "68b8fdef6ab1d999d21ccc8d29f08c6bf5fde8a5d56164dec9fc8a0649936023"
