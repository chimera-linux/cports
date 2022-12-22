pkgname = "libnice"
pkgver = "0.1.19"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared", "-Dcrypto-library=openssl",
    "-Dgtk_doc=disabled", "-Dexamples=disabled",
    "-Dintrospection=enabled", "-Dtests=enabled"
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection"
]
makedepends = [
    "gstreamer-devel", "openssl-devel", "libglib-devel"
]
pkgdesc = "Implementation of the IETF's draft ICE"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libnice.freedesktop.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "6747af710998cf708a2e8ceef51cccd181373d94201dd4b8d40797a070ed47cc"
# tests fail for now
options = ["!cross", "!check"]

@subpackage("libnice-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
