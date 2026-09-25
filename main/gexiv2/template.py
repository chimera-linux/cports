pkgname = "gexiv2"
pkgver = "0.16.2"
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
sha256 = "aad9e240fdffbe85e390f46ee0a567e251baea5c29c3d8690260388683dc8d0a"


@subpackage("gexiv2-devel")
def _(self):
    return self.default_devel()
