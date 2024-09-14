pkgname = "nautilus-python"
pkgver = "4.0.1"
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
source = f"{url}/-/archive/{pkgver}/nautilus-python-{pkgver}.tar.gz"
sha256 = "68c2cb1435addaccf19b8926bda2caf492e4e4273dfcf800acd87e967b8aaec0"
