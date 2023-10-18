pkgname = "eartag"
pkgver = "0.5.0"
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
checkdepends = list(depends) + ["python-pytest"]
pkgdesc = "Edit audio file tags"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.gnome.org/World/eartag"
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.bz2"
sha256 = "af09cc508abb62916b92e742ab1fa49daba6d8d7836dd1941e8cef1a3304f8b5"


def post_install(self):
    self.install_license("COPYING")
