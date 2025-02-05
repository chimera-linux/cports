pkgname = "file-roller"
pkgver = "44.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
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
    "nautilus-devel",
]
pkgdesc = "GNOME archiver frontend"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/FileRoller"
source = f"https://gitlab.gnome.org/GNOME/file-roller/-/archive/{pkgver}/file-roller-{pkgver}.tar.gz"
sha256 = "6a56bf1ef2f7c41d8659ba0d84026f263096999d1a908be6e7935e4ee72c0607"
