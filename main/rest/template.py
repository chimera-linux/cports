pkgname = "rest"
pkgver = "0.9.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dsoup2=false",
    "-Dgtk_doc=false",
    "-Dexamples=false",
    "-Dca_certificates=true",
    "-Dca_certificates_path=/etc/ssl/certs/ca-certificates.crt",
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
    "glib-devel",
    "json-glib-devel",
    "libsoup-devel",
    "libxml2-devel",
]
pkgdesc = "GNOME RESTful library"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/librest"
source = f"$(GNOME_SITE)/rest/{pkgver[:-2]}/rest-{pkgver}.tar.xz"
sha256 = "9266a5c10ece383e193dfb7ffb07b509cc1f51521ab8dad76af96ed14212c2e3"


@subpackage("rest-devel")
def _(self):
    return self.default_devel()
