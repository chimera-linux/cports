pkgname = "babl"
pkgver = "0.1.110"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable-gir=true", "-Dwith-docs=false"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala-devel",
]
makedepends = ["glib-devel", "lcms2-devel", "vala-devel"]
pkgdesc = "Dynamic pixel format translation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://gegl.org/babl"
source = (
    f"https://download.gimp.org/pub/babl/{pkgver[:-4]}/babl-{pkgver}.tar.xz"
)
sha256 = "bf47be7540d6275389f66431ef03064df5376315e243d0bab448c6aa713f5743"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _(self):
    return self.default_devel()
