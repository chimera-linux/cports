pkgname = "constrict"
pkgver = "26.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
depends = [
    "ffmpeg",
    "glycin-gtk4",
    "libadwaita",
    "python-gobject",
]
pkgdesc = "Compress videos to target sizes"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Constrict"
source = f"https://gitlab.gnome.org/World/Constrict/-/archive/{pkgver}/Constrict-{pkgver}.tar.gz"
sha256 = "082a8a3db65b7cfb86cee32f65160f9da31964fe9e5d142f78fb0765da1cf1d5"
