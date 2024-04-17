pkgname = "libshumate"
pkgver = "1.2.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsysprof=disabled", "-Dgtk_doc=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "gperf",
]
makedepends = [
    "glib-devel",
    "cairo-devel",
    "sqlite-devel",
    "gtk4-devel",
    "libsoup-devel",
    "json-glib-devel",
    "protobuf-c-devel",
]
pkgdesc = "GTK library to display maps"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/Maps"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4f8413a707cd00f84cee39ca49f58c48fc436f008ea80d6532ac37dafd0ba96b"
# FIXME
options = ["!check"] 

@subpackage("libshumate-devel")
def _devel(self):
    return self.default_devel()
