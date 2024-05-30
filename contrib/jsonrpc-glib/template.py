pkgname = "jsonrpc-glib"
pkgver = "3.44.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/jsonrpc-glib"
source = f"$(GNOME_SITE)/jsonrpc-glib/{'.'.join(pkgver.rsplit('.')[:-1])}/jsonrpc-glib-{pkgver}.tar.xz"
sha256 = "69406a0250d0cc5175408cae7eca80c0c6bfaefc4ae1830b354c0433bcd5ce06"
hardening = ["vis"]
# gobject-introspection
options = ["!cross"]


@subpackage("jsonrpc-glib-devel")
def _devel(self):
    return self.default_devel()
