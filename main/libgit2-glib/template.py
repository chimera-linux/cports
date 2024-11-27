pkgname = "libgit2-glib"
pkgver = "1.2.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "libgit2-devel",
    "libssh2-devel",
    "python-gobject-devel",
]
pkgdesc = "GLib wrapper around libgit2"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libgit2-glib"
source = f"$(GNOME_SITE)/libgit2-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/libgit2-glib-{pkgver}.tar.xz"
sha256 = "1331dada838f4e1f591b26459d44126a325de762dc3cd26153a31afbdfe18190"
# cross: gobject-introspection
# FIXME check: test uses IBM862 encoding so it fails in utf8
options = ["!cross", "!check"]


@subpackage("libgit2-glib-devel")
def _(self):
    return self.default_devel()
