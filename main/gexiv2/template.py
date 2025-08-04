pkgname = "gexiv2"
pkgver = "0.14.6"
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
sha256 = "606c28aaae7b1f3ef5c8eabe5e7dffd7c5a1c866d25b7671fb847fe287a72b8b"


@subpackage("gexiv2-devel")
def _(self):
    return self.default_devel()
