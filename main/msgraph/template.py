pkgname = "msgraph"
pkgver = "0.3.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=false"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gnome-online-accounts-devel",
    "json-glib-devel",
    "libsoup-devel",
]
checkdepends = ["libxml2-devel", "uhttpmock-devel"]
pkgdesc = "GLib-based library for MS Graph protocol"
license = "LGPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/msgraph"
source = f"$(GNOME_SITE)/msgraph/{pkgver[:-2]}/msgraph-{pkgver}.tar.xz"
sha256 = "37d7e12f2a990490aea21184f0b27e0b915ebb4e5096f4d6632c62051c054012"
options = ["!cross"]


@subpackage("msgraph-devel")
def _(self):
    return self.default_devel()
