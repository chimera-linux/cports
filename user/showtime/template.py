pkgname = "showtime"
pkgver = "48.0"
pkgrel = 0
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
sha256 = "b68cdcffe76ecd5c11a51939552879d8a4680d8b16022273f9c6fb162fd6c95a"
