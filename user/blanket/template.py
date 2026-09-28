pkgname = "blanket"
pkgver = "0.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "appstream-glib-devel",
    "blueprint-compiler",
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
depends = [
    "gst-plugins-base",
    "gtk4",
    "libadwaita",
    "python-gobject",
]
pkgdesc = "Listen to different sounds"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Blanket"
source = f"https://github.com/rafaelmardojai/blanket/archive/{pkgver}/blanket-{pkgver}.tar.gz"
sha256 = "46bc401182a738d9b4986b7491dfe330127117a511c24b81309b49ed5b9e6e83"


def post_install(self):
    self.install_license("COPYING")
