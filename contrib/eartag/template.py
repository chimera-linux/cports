pkgname = "eartag"
pkgver = "0.5.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
]
depends = [
    "gtk4",
    "libadwaita",
    "mutagen",
    "python-gobject",
    "python-magic",
    "python-pillow",
    "python-pyacoustid",
]
checkdepends = depends + ["python-pytest"]
pkgdesc = "Edit audio file tags"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.gnome.org/World/eartag"
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.bz2"
sha256 = "6b92a003a67ee7c8901d05dbd6a634e49a24d7d2df35ecf49101e498ab34bb0a"


def post_install(self):
    self.install_license("COPYING")
