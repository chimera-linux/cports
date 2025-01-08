pkgname = "eartag"
pkgver = "0.6.4"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://apps.gnome.org/EarTag"
source = f"https://gitlab.gnome.org/World/eartag/-/archive/{pkgver}/eartag-{pkgver}.tar.gz"
sha256 = "b2fe856dbd3534630b4de1f51b031f6c29eb1ce679769b6304e2f5ad056c7716"


def post_install(self):
    self.install_license("COPYING")
