pkgname = "eartag"
pkgver = "0.6.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
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
checkdepends = ["python-pytest", *depends]
pkgdesc = "Edit audio file tags"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://apps.gnome.org/EarTag"
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.bz2"
sha256 = "952d339caf74ed842a13a8039b6d97c0203581d97b1d47dc7da2e094c8f755ae"


def post_install(self):
    self.install_license("COPYING")
