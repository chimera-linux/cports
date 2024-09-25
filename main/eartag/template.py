pkgname = "eartag"
pkgver = "0.6.2"
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
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.gz"
sha256 = "2684a34550c43fda7f42f6ae49feac80ca21e843cd3503012eff58bda17383ed"


def post_install(self):
    self.install_license("COPYING")
