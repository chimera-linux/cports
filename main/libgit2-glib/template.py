pkgname = "libgit2-glib"
pkgver = "1.2.1"
pkgrel = 0
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libgit2-glib"
source = f"$(GNOME_SITE)/libgit2-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/libgit2-glib-{pkgver}.tar.xz"
sha256 = "97423a779002b3be8751c75f9d79049dfccca3616a26159fc162486772ba785f"
# cross: gobject-introspection
# FIXME check: test uses IBM862 encoding so it fails in utf8
options = ["!cross", "!check"]


@subpackage("libgit2-glib-devel")
def _(self):
    return self.default_devel()
