pkgname = "eartag"
pkgver = "0.4.3"
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
sha256 = "ff3afabc752059bdd62e554c41e5bdbc569dae397a8ec2689c7c99a972d0c073"


def post_install(self):
    self.install_license("COPYING")
