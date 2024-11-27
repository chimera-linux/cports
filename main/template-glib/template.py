pkgname = "template-glib"
pkgver = "3.36.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bison",
    "flex",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
pkgdesc = "Library for GObject template expansion"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/template-glib"
source = f"$(GNOME_SITE)/template-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/template-glib-{pkgver}.tar.xz"
sha256 = "0020f3a401888ce763b3a17508c2f58e91972a483a0c547afdb7ccbe25619948"
# gobject-introspection
options = ["!cross"]


@subpackage("template-glib-devel")
def _(self):
    return self.default_devel()
