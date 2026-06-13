pkgname = "drawing"
pkgver = "1.0.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "Simple drawing program"
license = "GPL-3.0-or-later"
url = "https://github.com/maoschanz/drawing"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "539e7e28fe4db96cfedd4477e217d5d48b9422ad8c98f33d8ae46120b2d5738b"
