pkgname = "jsonrpc-glib"
pkgver = "3.44.2"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/jsonrpc-glib"
source = f"$(GNOME_SITE)/jsonrpc-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/jsonrpc-glib-{pkgver}.tar.xz"
sha256 = "965496b6e1314f3468b482a5d80340dc3b0340a5402d7783cad24154aee77396"
hardening = ["vis"]
# gobject-introspection
options = ["!cross"]


@subpackage("jsonrpc-glib-devel")
def _(self):
    return self.default_devel()
