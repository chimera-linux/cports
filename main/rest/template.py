pkgname = "rest"
pkgver = "0.9.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dca_certificates=true", "-Dsoup2=false", "-Dgtk_doc=false",
    "-Dca_certificates_path=/etc/ssl/certs/ca-certificates.crt"
]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "vala",
]
makedepends = [
    "libglib-devel", "libsoup-devel", "json-glib-devel", "libxml2-devel"
]
pkgdesc = "GNOME RESTful library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/librest"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "85b2bc9341128139539b53ee53f0533310bc96392fd645863a040410b81ebe66"

@subpackage("rest-devel")
def _devel(self):
    return self.default_devel()
