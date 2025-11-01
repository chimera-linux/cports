pkgname = "orca"
pkgver = "49.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    # checks for gtk+3 by running python program in host :/
    "gtk+3",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
    "python-dasbus",
    "python-gobject",
]
makedepends = [
    "at-spi2-core-devel",
    "python-gobject-devel",
]
depends = [
    "at-spi2-core",
    "gstreamer",
    "gtk+3",
    "libwnck",
    "python-dasbus",
    "python-gobject",
    "python-psutil",
    "python-setproctitle",
    "speechd",
    # TODO: liblouis, brlapi, brltty,
]
pkgdesc = "GNOME screen reader"
license = "LGPL-2.1-or-later"
url = "https://orca.gnome.org"
source = f"$(GNOME_SITE)/orca/{pkgver[:-2]}/orca-{pkgver}.tar.xz"
sha256 = "b6ba4cc5878411c34a7d5b7ee9b2c5c9b1d04add10bfd20f6e2331d594165207"


def post_install(self):
    self.uninstall("usr/lib/systemd")
