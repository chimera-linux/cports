pkgname = "template-glib"
pkgver = "3.38.0"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/template-glib"
source = f"$(GNOME_SITE)/template-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/template-glib-{pkgver}.tar.xz"
sha256 = "40d00dc223dcf2eb7f2ec422f7dec5a67373a0ca1101abca0f49c62f050cb312"
# gobject-introspection
options = ["!cross"]


@subpackage("template-glib-devel")
def _(self):
    return self.default_devel()
