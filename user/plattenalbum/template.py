pkgname = "plattenalbum"
pkgver = "2.3.1"
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
depends = ["gtk4", "libadwaita", "mpd", "python-gobject", "python-mpd2"]
pkgdesc = "Simple music browser for MPD"
license = "GPL-3.0-or-later"
url = "https://github.com/SoongNoonien/plattenalbum"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "501aec33f26065d1ccdeee3b2233a3148015d8d84599aa886dd0a1331a83b348"


def post_install(self):
    self.install_license("LICENSE")
