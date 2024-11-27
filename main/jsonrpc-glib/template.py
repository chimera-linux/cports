pkgname = "jsonrpc-glib"
pkgver = "3.44.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["json-glib-devel"]
pkgdesc = "Library for the JSON-RPC 2.0 specification"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/jsonrpc-glib"
source = f"$(GNOME_SITE)/jsonrpc-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/jsonrpc-glib-{pkgver}.tar.xz"
sha256 = "1361d17e9c805646afe5102e59baf8ca450238600fcabd01586c654b78bb30df"
hardening = ["vis"]
# gobject-introspection
options = ["!cross"]


@subpackage("jsonrpc-glib-devel")
def _(self):
    return self.default_devel()
