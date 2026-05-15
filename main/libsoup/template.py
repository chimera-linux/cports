pkgname = "libsoup"
pkgver = "3.6.6"
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
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "brotli-devel",
    "glib-devel",
    "glib-networking",
    "heimdal-devel",
    "libpsl-devel",
    "libxml2-devel",
    "nghttp2-devel",
    "sqlite-devel",
    "vala-devel",
]
depends = ["glib-networking"]
pkgdesc = "HTTP library for glib"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsoup"
source = f"$(GNOME_SITE)/libsoup/{pkgver[:-2]}/libsoup-{pkgver}.tar.xz"
sha256 = "51ed0ae06f9d5a40f401ff459e2e5f652f9a510b7730e1359ee66d14d4872740"
# krb5-config may be problematic
options = ["!cross"]


@subpackage("libsoup-devel")
def _(self):
    return self.default_devel()
