pkgname = "showtime"
pkgver = "49.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = ["libadwaita-devel"]
depends = [
    "gst-plugins-base",
    "gst-plugins-rs-gtk4",
    "libadwaita",
    "python-gobject",
]
pkgdesc = "GNOME video player"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/Incubator/showtime"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "34ebe1ff67e14d9dd3b99a7eddd467f50c0492eee56410f17cf865a503df0285"
