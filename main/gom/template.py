pkgname = "gom"
pkgver = "0.5.4"
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
sha256 = "57ba806fe080a937d5664178d21bad7653b2c561ea128187a7b10bc1762b7f65"
options = ["!cross"]


@subpackage("gom-devel")
def _(self):
    return self.default_devel()


@subpackage("gom-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python-gobject"]

    return ["usr/lib/python*"]
