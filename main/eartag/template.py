pkgname = "eartag"
pkgver = "1.0.2"
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
    "python-filetype",
    "python-gobject",
    "python-magic",
    "python-pillow",
    "python-pyacoustid",
]
pkgdesc = "Edit audio file tags"
license = "MIT"
url = "https://apps.gnome.org/EarTag"
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.gz"
sha256 = "c11287ba47fb529b44163e0fbdd1950efd7b9fd970fdfe7027e86bb93decf1b9"
# requires multiple unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
