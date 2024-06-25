pkgname = "orca"
pkgver = "46.2"
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
sha256 = "8f63299b1a4f9c30857c229f6a9ce16f2c43eaeea90fbf909314ca8bb73efd5e"
