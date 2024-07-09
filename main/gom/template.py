pkgname = "gom"
pkgver = "0.5.2"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gom"
source = f"$(GNOME_SITE)/gom/{pkgver[:-2]}/gom-{pkgver}.tar.xz"
sha256 = "4cde83adf6f826836ed575d420f987ad1f559606b218224b69bf559f2ed7e205"
options = ["!cross"]


@subpackage("gom-devel")
def _devel(self):
    return self.default_devel()


@subpackage("gom-python")
def _python(self):
    self.subdesc = "Python bindings"
    self.depends += ["python-gobject"]

    return ["usr/lib/python*"]
