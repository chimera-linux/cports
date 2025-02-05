pkgname = "libnice"
pkgver = "0.1.22"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dcrypto-library=openssl",
    "-Dgtk_doc=disabled",
    "-Dexamples=disabled",
    "-Dintrospection=enabled",
    "-Dtests=enabled",
]
hostmakedepends = ["glib-devel", "gobject-introspection", "meson", "pkgconf"]
makedepends = ["glib-devel", "gstreamer-devel", "openssl3-devel"]
pkgdesc = "Implementation of the IETF's draft ICE"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://libnice.freedesktop.org"
source = f"{url}/releases/libnice-{pkgver}.tar.gz"
sha256 = "a5f724cf09eae50c41a7517141d89da4a61ec9eaca32da4a0073faed5417ad7e"
options = ["!cross"]


@subpackage("libnice-devel")
def _(self):
    return self.default_devel()
