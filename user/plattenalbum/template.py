pkgname = "plattenalbum"
pkgver = "2.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
depends = ["libadwaita", "python-gobject", "python-mpd2"]
pkgdesc = "MPD client"
license = "GPL-3.0-or-later"
url = "https://github.com/SoongNoonien/plattenalbum"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "20e400a4b30edc5db9ee4942ffe386b4fede5695623b4af28f999317a473b1d5"


def post_install(self):
    self.install_license("LICENSE")
