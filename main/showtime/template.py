pkgname = "showtime"
pkgver = "50.0"
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
sha256 = "d734e0f9618bc0c94976407eb68604f57a16a34f0dad30c91054c30c330aeadc"
