pkgname = "libsoup"
pkgver = "3.4.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgssapi=enabled", "-Dbrotli=enabled", "-Dintrospection=enabled",
    "-Dvapi=enabled", "-Dntlm=disabled", "-Dsysprof=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "vala", "glib-devel",
    "gettext-tiny"
]
makedepends = [
    "glib-devel", "libxml2-devel", "sqlite-devel", "nghttp2-devel",
    "brotli-devel", "libpsl-devel", "vala-devel", "heimdal-devel",
    "glib-networking",
]
depends = ["glib-networking"]
pkgdesc = "HTTP library for glib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsoup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "530b867b1b166cb9bca2750f1d15e5187318b5d948efb81d5899af3d75614504"
# krb5-config may be problematic
options = ["!cross"]

@subpackage("libsoup-devel")
def _devel(self):
    return self.default_devel()
