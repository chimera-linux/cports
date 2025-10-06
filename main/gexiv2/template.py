pkgname = "gexiv2"
pkgver = "0.16.0"
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
url = "https://gitlab.gnome.org/GNOME/gexiv2"
source = f"$(GNOME_SITE)/gexiv2/{pkgver[:-2]}/gexiv2-{pkgver}.tar.xz"
sha256 = "d96f895f24539f966f577b2bb2489ae84f8232970a8d0c064e4a007474a77bbb"


@subpackage("gexiv2-devel")
def _(self):
    return self.default_devel()
