pkgname = "orca"
pkgver = "47_rc"
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
source = (
    f"$(GNOME_SITE)/orca/{pkgver[:2]}/orca-{pkgver.replace('_', '.')}.tar.xz"
)
sha256 = "6d258d171b3098eec0c32cdaf87ca6e2f883f2c01fff84e826af629ccb237222"
