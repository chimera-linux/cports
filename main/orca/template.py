pkgname = "orca"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
# needs rust
configure_args = ["-Dmathcat=false"]
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
sha256 = "8bc3e44bc5b7b66ec7e0cc5c82695c0075661922745d25724f5fc84a25602108"
options = ["etcfiles"]


def post_install(self):
    self.uninstall("usr/lib/systemd")
