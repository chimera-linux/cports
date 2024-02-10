pkgname = "babl"
pkgver = "0.1.108"
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
sha256 = "26defe9deaab7ac4d0e076cab49c2a0d6ebd0df0c31fd209925a5f07edee1475"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _devel(self):
    return self.default_devel()
