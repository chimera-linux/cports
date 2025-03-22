pkgname = "babl"
pkgver = "0.1.112"
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
license = "LGPL-3.0-only"
url = "https://gegl.org/babl"
source = (
    f"https://download.gimp.org/pub/babl/{pkgver[:-4]}/babl-{pkgver}.tar.xz"
)
sha256 = "fb696682421787c8fecc83e8aab48121dec8ee38d119b65291cfcbe315028a79"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _(self):
    return self.default_devel()
