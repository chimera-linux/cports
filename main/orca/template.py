pkgname = "orca"
pkgver = "47.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    # checks for gtk+3 by running python program in host :/
    "gtk+3",
    "gtk-update-icon-cache",
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
    "python-gobject",
    "python-psutil",
    "python-setproctitle",
    "speechd",
    # TODO: liblouis, brlapi, brltty,
]
pkgdesc = "GNOME screen reader"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://orca.gnome.org"
source = f"$(GNOME_SITE)/orca/{pkgver[:-2]}/orca-{pkgver}.tar.xz"
sha256 = "5e67af357f7198ea00a44381cab4c4f94e6826d6ed800668f39416ce2aab8e5a"
