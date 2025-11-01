pkgname = "gom"
pkgver = "0.5.5"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-gobject",
]
makedepends = ["gdk-pixbuf-devel", "glib-devel", "sqlite-devel"]
pkgdesc = "GObject data mapper"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gom"
source = f"$(GNOME_SITE)/gom/{pkgver[:-2]}/gom-{pkgver}.tar.xz"
sha256 = "ad61f05af2317a7ab1771fcfa816989fbba3b18957d2e0b5dede9ef45f09b534"
# introspection
options = ["!cross"]


@subpackage("gom-devel")
def _(self):
    return self.default_devel()


@subpackage("gom-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python-gobject"]

    return ["usr/lib/python*"]
