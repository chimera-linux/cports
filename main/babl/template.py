pkgname = "babl"
pkgver = "0.1.106"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable-gir=true", "-Dwith-docs=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gobject-introspection",
    "vala-devel",
]
makedepends = ["glib-devel", "lcms2-devel", "vala-devel"]
pkgdesc = "Dynamic pixel format translation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://gegl.org/babl"
source = f"https://download.gimp.org/pub/{pkgname}/{pkgver[:-4]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d325135d3304f088c134cc620013acf035de2e5d125a50a2d91054e7377c415f"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _devel(self):
    return self.default_devel()
