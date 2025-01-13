pkgname = "libsoup"
pkgver = "3.6.3"
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
sha256 = "a0d84ab07bd168b317d319b0dc40c8b301b4543fba2ec42fa733914b2081afbd"
# krb5-config may be problematic
options = ["!cross"]


@subpackage("libsoup-devel")
def _(self):
    return self.default_devel()
