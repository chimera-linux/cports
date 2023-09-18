pkgname = "libsoup"
pkgver = "3.4.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgssapi=enabled",
    "-Dbrotli=enabled",
    "-Dintrospection=enabled",
    "-Dvapi=enabled",
    "-Dntlm=disabled",
    "-Dsysprof=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
    "glib-devel",
    "gettext",
]
makedepends = [
    "glib-devel",
    "libxml2-devel",
    "sqlite-devel",
    "nghttp2-devel",
    "brotli-devel",
    "libpsl-devel",
    "vala-devel",
    "heimdal-devel",
    "glib-networking",
]
depends = ["glib-networking"]
pkgdesc = "HTTP library for glib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsoup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b7f1bbaeeb43f5812daba3ee258a72e1b4b14c2fd91f4a1a75d4eea10dcf288f"
# krb5-config may be problematic
options = ["!cross"]


@subpackage("libsoup-devel")
def _devel(self):
    return self.default_devel()
