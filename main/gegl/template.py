pkgname = "gegl"
pkgver = "0.4.68"
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
    "-Dlibav=disabled",  # tests fail
    "-Dsdl2=disabled",
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
    "ffmpeg-devel",
    "gexiv2-devel",
    "jasper-devel",
    "json-glib-devel",
    "lensfun-devel",
    "libraw-devel",
    "librsvg-devel",
    "libspiro-devel",
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
sha256 = "5002309b9a701260658e8b3a61540fd5673887cef998338e1992524a33b23ae3"
# TODO
hardening = ["!int"]

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]


@subpackage("gegl-devel")
def _(self):
    return self.default_devel()
