pkgname = "gedit"
pkgver = "40.1"
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
provides = ["so:libgedit-40.0.so=0"]
pkgdesc = "GNOME text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Gedit"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "55e394a82cb65678b1ab49526cf5bd43f00d8fba21476a4849051a8e137d3691"
pycompile_dirs = ["usr/lib/gedit/plugins"]

@subpackage("gedit-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
