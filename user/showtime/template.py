pkgname = "showtime"
pkgver = "47.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/Incubator/showtime"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "31deffae0be27851068b35f23e04ef36189759c4466e2d13e0127550fec0b772"
