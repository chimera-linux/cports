pkgname = "file-roller"
pkgver = "44.6"
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
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/FileRoller"
source = f"https://gitlab.gnome.org/GNOME/file-roller/-/archive/{pkgver}/file-roller-{pkgver}.tar.gz"
sha256 = "57567a1d8320aaba9131832aadce72a8845052e8105c0734cc2713b323f911a1"
