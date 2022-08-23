pkgname = "libsoup"
pkgver = "3.1.3"
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
    "libglib-devel", "libxml2-devel", "sqlite-devel", "nghttp2-devel",
    "brotli-devel", "libpsl-devel", "vala-devel", "heimdal-devel",
    "glib-networking",
]
depends = ["glib-networking"]
pkgdesc = "HTTP library for glib"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsoup"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d8aa9537a164ea6fbbda8858f28cc63d880fc4418c9beed3de625ed971eb59a7"
# krb5-config may be problematic
options = ["!cross"]

@subpackage("libsoup-devel")
def _devel(self):
    return self.default_devel()
