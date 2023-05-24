pkgname = "gedit"
pkgver = "44.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext-tiny",
    "vala",
    "gobject-introspection",
    "perl",
    "itstool",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "libpeas-devel",
    "gspell-devel",
    "libxml2-devel",
    "python-gobject-devel",
    "tepl-devel",
    "amtk-devel",
]
depends = ["gsettings-desktop-schemas", "iso-codes", "python-gobject"]
provides = ["so:libgedit-44.so=0"]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Gedit"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3bbb1b3775d4c277daf54aaab44b0eb83a4eb1f09f0391800041c9e56893ec11"


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib/gedit/plugins")


@subpackage("gedit-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
