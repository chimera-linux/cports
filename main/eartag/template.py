pkgname = "eartag"
pkgver = "0.6.5"
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
license = "MIT"
url = "https://apps.gnome.org/EarTag"
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.gz"
sha256 = "122093d2e17cc6f242bd5effac9e9ac0d320b9124a98b7cb638f19cb324d8269"


def post_install(self):
    self.install_license("COPYING")
