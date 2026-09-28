pkgname = "librest"
pkgver = "0.10.2"
pkgrel = 0
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
renames = ["rest"]
pkgdesc = "GNOME RESTful library"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/librest"
source = f"$(GNOME_SITE)/librest/{pkgver[:-2]}/librest-{pkgver}.tar.xz"
sha256 = "7b6cb912bb3a22cfa7dcf005925dcb62883024db0c09099486e7d6851185c9b8"


@subpackage("librest-devel")
def _(self):
    self.renames = ["rest-devel"]
    return self.default_devel()
