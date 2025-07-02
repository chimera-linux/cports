pkgname = "orca"
pkgver = "48.6"
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
    "python-dbus",
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
sha256 = "edc50344e0dfd72476b5c14b3aa725ca268718ea6dd89bc4ee26f450b339d696"
