pkgname = "libpeas"
pkgver = "1.36.0"
pkgrel = 4
build_style = "meson"
configure_args = ["-Ddemos=false", "-Dvapi=true"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "python-devel",
    "python-gobject-devel",
]
depends = ["python-gobject"]
checkdepends = ["xwayland-run", "fonts-dejavu-ttf"]
pkgdesc = "GObject application plugin library (1.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Libpeas"
source = f"$(GNOME_SITE)/libpeas/{pkgver[:-2]}/libpeas-{pkgver}.tar.xz"
sha256 = "297cb9c2cccd8e8617623d1a3e8415b4530b8e5a893e3527bbfd1edd13237b4c"
# gtk3 can't handle seatless wayland displays
options = ["!cross", "!check"]


@subpackage("libpeas-devel")
def _devel(self):
    return self.default_devel()
