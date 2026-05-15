pkgname = "libnice"
pkgver = "0.1.23"
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
makedepends = [
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "openssl3-devel",
]
pkgdesc = "Implementation of the IETF's draft ICE"
license = "LGPL-2.1-or-later"
url = "https://libnice.freedesktop.org"
source = f"{url}/releases/libnice-{pkgver}.tar.gz"
sha256 = "618fc4e8de393b719b1641c1d8eec01826d4d39d15ade92679d221c7f5e4e70d"
options = ["!cross"]


@subpackage("libnice-devel")
def _(self):
    return self.default_devel()
