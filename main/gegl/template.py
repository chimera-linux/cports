pkgname = "gegl"
pkgver = "0.4.54"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dintrospection=true",
    "-Dvapigen=enabled",
    "-Dlibspiro=disabled",
    "-Dlua=disabled",
    "-Dmrg=disabled",
    "-Dopenexr=enabled",
    "-Dsdl2=disabled",
    "-Dlibav=disabled",
    "-Dumfpack=disabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala-devel",
    "gettext",
]
makedepends = [
    "babl-devel",
    "exiv2-devel",
    "gexiv2-devel",
    "librsvg-devel",
    "libraw-devel",
    "libwebp-devel",
    "openexr-devel",
    "pango-devel",
    "poppler-devel",
    "lensfun-devel",
    "v4l-utils-devel",
    "json-glib-devel",
    "vala-devel",
]
pkgdesc = "Graph-based image processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-3.0-only"
url = "https://gegl.org"
source = (
    f"https://download.gimp.org/pub/gegl/{pkgver[:-3]}/gegl-{pkgver}.tar.xz"
)
sha256 = "35a342f08c6b4379adee2cb5748fc4e307cfdcf2417c0bb17d6ca6543f238b1e"
# TODO
hardening = ["!int"]


@subpackage("gegl-devel")
def _(self):
    return self.default_devel()
