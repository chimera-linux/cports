pkgname = "nautilus-python"
pkgver = "4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "nautilus-devel",
    "python-devel",
    "python-gobject-devel",
]
depends = [
    "python-gobject",
]
pkgdesc = "Python plugin support for Nautilus"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/nautilus-python"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2f85820d5033383271032169b1fbf7ee71d495a4562f6f1912849b12d5c9f9cc"
