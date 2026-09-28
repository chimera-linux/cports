pkgname = "libgxps"
pkgver = "0.3.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable-test=false", "-Ddisable-introspection=false"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "freetype-devel",
    "glib-devel",
    "lcms2-devel",
    "libarchive-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
]
pkgdesc = "GObject library for XPS documents"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/libgxps"
source = f"$(GNOME_SITE)/libgxps/{pkgver[:-2]}/libgxps-{pkgver}.tar.xz"
sha256 = "6d27867256a35ccf9b69253eb2a88a32baca3b97d5f4ef7f82e3667fa435251c"


@subpackage("libgxps-devel")
def _(self):
    return self.default_devel()
