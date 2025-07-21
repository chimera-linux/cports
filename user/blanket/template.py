pkgname = "blanket"
pkgver = "0.7.0"
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
sha256 = "14445e5d2b56116ac741aef8bba9fed444ec52a089ebd175099539a87de10ab5"


def post_install(self):
    self.install_license("COPYING")
