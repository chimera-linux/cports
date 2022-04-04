pkgname = "gedit"
pkgver = "42.0"
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
sha256 = "a87991f42961eb4f6abcdbaabb784760c23aeaeefae6363d3e21a61e9c458437"

def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib/gedit/plugins")

@subpackage("gedit-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
