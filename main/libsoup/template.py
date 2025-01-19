pkgname = "libsoup"
pkgver = "3.6.4"
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
source = f"$(GNOME_SITE)/libsoup/{pkgver[:-2]}/libsoup-{pkgver}.tar.xz"
sha256 = "9b54c76f5276b05bebcaf2b6c2a141a188fc7bb1d0624eda259dac13a6665c8a"
# krb5-config may be problematic
options = ["!cross"]


@subpackage("libsoup-devel")
def _(self):
    return self.default_devel()
