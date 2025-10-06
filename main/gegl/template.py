pkgname = "gegl"
pkgver = "0.4.64"
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
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python",
    "vala-devel",
]
makedepends = [
    "babl-devel",
    "exiv2-devel",
    "gexiv2-devel",
    "json-glib-devel",
    "lensfun-devel",
    "libraw-devel",
    "librsvg-devel",
    "libwebp-devel",
    "openexr-devel",
    "pango-devel",
    "poppler-devel",
    "v4l-utils-devel",
    "vala-devel",
]
pkgdesc = "Graph-based image processing framework"
license = "GPL-3.0-only AND LGPL-3.0-only"
url = "https://gegl.org"
source = (
    f"https://download.gimp.org/pub/gegl/{pkgver[:-3]}/gegl-{pkgver}.tar.xz"
)
sha256 = "0de1c9dd22c160d5e4bdfc388d292f03447cca6258541b9a12fed783d0cf7c60"
# TODO
hardening = ["!int"]


@subpackage("gegl-devel")
def _(self):
    return self.default_devel()
