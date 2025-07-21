pkgname = "gexiv2"
pkgver = "0.14.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Dvapi=true"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-gobject",
    "vala",
]
makedepends = ["glib-devel", "exiv2-devel"]
pkgdesc = "GObject wrapper for exiv2"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gexiv2"
source = f"$(GNOME_SITE)/gexiv2/{pkgver[:-2]}/gexiv2-{pkgver}.tar.xz"
sha256 = "0913c53daabab1f1ab586afd55bb55370796f2b8abcc6e37640ab7704ad99ce1"


@subpackage("gexiv2-devel")
def _(self):
    return self.default_devel()
