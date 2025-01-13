pkgname = "template-glib"
pkgver = "3.36.3"
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
sha256 = "d528b35b2cf90e07dae50e25e12fbadb0eb048f57fd5151cf9f6e98cce1df20e"
# gobject-introspection
options = ["!cross"]


@subpackage("template-glib-devel")
def _(self):
    return self.default_devel()
