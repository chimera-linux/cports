pkgname = "nautilus-python"
pkgver = "4.1.0"
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
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/nautilus-python"
source = f"{url}/-/archive/{pkgver}/nautilus-python-{pkgver}.tar.gz"
sha256 = "02803bb8dc7eb8dd14ccdf3e042010d8c20750fbbac8c15702e9774ec7a3eeb6"
