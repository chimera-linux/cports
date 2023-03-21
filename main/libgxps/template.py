pkgname = "libgxps"
pkgver = "0.3.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable-test=false", "-Ddisable-introspection=false"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection",
]
makedepends = [
    "glib-devel", "cairo-devel", "freetype-devel", "libarchive-devel",
    "libpng-devel", "lcms2-devel", "libjpeg-turbo-devel", "libtiff-devel",
]
pkgdesc = "GObject library for XPS documents"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/libgxps"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6d27867256a35ccf9b69253eb2a88a32baca3b97d5f4ef7f82e3667fa435251c"

@subpackage("libgxps-devel")
def _devel(self):
    return self.default_devel()
