pkgname = "orca"
pkgver = "50.1.2"
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
source = f"$(GNOME_SITE)/orca/{pkgver[:-4]}/orca-{pkgver}.tar.xz"
sha256 = "8592b53df84239ea75ddaa8dec6792c84d2b99fb7b47a5fd9022c6af8ca657a8"


def post_install(self):
    self.uninstall("usr/lib/systemd")
