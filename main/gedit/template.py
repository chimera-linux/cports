pkgname = "gedit"
pkgver = "42.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala",
    "gobject-introspection", "perl", "itstool",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "gtksourceview4-devel", "libpeas-devel",
    "gspell-devel", "libxml2-devel", "python-gobject-devel",
]
depends = ["gsettings-desktop-schemas", "iso-codes", "python-gobject"]
provides = ["so:libgedit-41.0.so=0"]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Gedit"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3c6229111f0ac066ae44964920791d1265f5bbb56b0bd949a69b7b1261fc8fca"

def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib/gedit/plugins")

@subpackage("gedit-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
