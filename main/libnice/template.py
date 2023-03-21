pkgname = "libnice"
pkgver = "0.1.21"
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
    "gstreamer-devel", "openssl-devel", "glib-devel"
]
pkgdesc = "Implementation of the IETF's draft ICE"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libnice.freedesktop.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "72e73a2acf20f59093e21d5601606e405873503eb35f346fa621de23e99b3b39"
# tests fail for now
options = ["!cross", "!check"]

@subpackage("libnice-devel")
def _devel(self):
    return self.default_devel()
