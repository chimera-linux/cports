pkgname = "gexiv2"
pkgver = "0.14.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Dvapi=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "python-gobject",
    "vala",
]
makedepends = ["glib-devel", "exiv2-devel"]
pkgdesc = "GObject wrapper for exiv2"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gexiv2"
source = f"$(GNOME_SITE)/gexiv2/{pkgver[:-2]}/gexiv2-{pkgver}.tar.xz"
sha256 = "21e64d2c56e9b333d44fef3f2a4b25653d922c419acd972fa96fab695217e2c8"


@subpackage("gexiv2-devel")
def _(self):
    return self.default_devel()
