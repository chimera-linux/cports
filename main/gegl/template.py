pkgname = "gegl"
pkgver = "0.4.44"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false", "-Dintrospection=true", "-Dvapigen=enabled",
    "-Dlibspiro=disabled", "-Dlua=disabled", "-Dmrg=disabled",
    "-Dopenexr=disabled", "-Dsdl2=disabled", "-Dlibav=disabled",
    "-Dumfpack=disabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gobject-introspection", "vala-devel",
    "gettext-tiny",
]
makedepends = [
    "babl-devel", "exiv2-devel", "gexiv2-devel", "librsvg-devel",
    "libraw-devel", "libwebp-devel", "libpoppler-glib-devel", "pango-devel",
    "lensfun-devel", "v4l-utils-devel", "json-glib-devel", "vala-devel",
]
pkgdesc = "Graph-based image processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-3.0-only"
url = "https://gegl.org"
source = f"https://download.gimp.org/pub/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0a4cdb41635e406a0849cd0d3f03caf7d97cab8aa13d28707d532d0089d56126"
# TODO
hardening = ["!int"]

@subpackage("gegl-devel")
def _devel(self):
    return self.default_devel()
