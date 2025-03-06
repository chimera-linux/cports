pkgname = "gom"
pkgver = "0.5.3"
pkgrel = 1
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
sha256 = "069d0909fbdc6b4d27edf7a879366194e3ab508b03548bf5b89ff63546d20177"
options = ["!cross"]


@subpackage("gom-devel")
def _(self):
    return self.default_devel()


@subpackage("gom-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python-gobject"]

    return ["usr/lib/python*"]
