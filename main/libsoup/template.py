pkgname = "libsoup"
pkgver = "3.6.5"
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
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsoup"
source = f"$(GNOME_SITE)/libsoup/{pkgver[:-2]}/libsoup-{pkgver}.tar.xz"
sha256 = "6891765aac3e949017945c3eaebd8cc8216df772456dc9f460976fbdb7ada234"
# krb5-config may be problematic
options = ["!cross"]


@subpackage("libsoup-devel")
def _(self):
    return self.default_devel()
