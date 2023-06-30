pkgname = "gegl"
pkgver = "0.4.46"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocs=false",
    "-Dintrospection=true",
    "-Dvapigen=enabled",
    "-Dlibspiro=disabled",
    "-Dlua=disabled",
    "-Dmrg=disabled",
    "-Dopenexr=disabled",
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
    "gettext-tiny",
]
makedepends = [
    "babl-devel",
    "exiv2-devel",
    "gexiv2-devel",
    "librsvg-devel",
    "libraw-devel",
    "libwebp-devel",
    "libpoppler-glib-devel",
    "pango-devel",
    "lensfun-devel",
    "v4l-utils-devel",
    "json-glib-devel",
    "vala-devel",
]
pkgdesc = "Graph-based image processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-only AND LGPL-3.0-only"
url = "https://gegl.org"
source = f"https://download.gimp.org/pub/{pkgname}/{pkgver[:-3]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d0b3b2481bc8774c5f3d0a487611910166d18eef823a859fb91e781ab7b1e892"
# TODO
hardening = ["!int"]


@subpackage("gegl-devel")
def _devel(self):
    # some .so's should remain in main package
    return [
        "usr/include/gegl-0.4",
        "usr/lib/libgegl-0.4.so",
        "usr/lib/*.a",
        "usr/lib/pkgconfig",
        "usr/share/gir-1.0",
        "usr/share/vala/vapi",
    ]
