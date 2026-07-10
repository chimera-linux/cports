pkgname = "babl"
pkgver = "0.1.126"
pkgrel = 0
build_style = "meson"
configure_args = ["-Denable-gir=true", "-Dwith-docs=false"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python",
    "vala-devel",
]
makedepends = ["glib-devel", "lcms2-devel", "vala-devel"]
pkgdesc = "Dynamic pixel format translation library"
license = "LGPL-3.0-only"
url = "https://gegl.org/babl"
source = (
    f"https://download.gimp.org/pub/babl/{pkgver[:-4]}/babl-{pkgver}.tar.xz"
)
sha256 = "3f090f4b2a61fecf7c8dc60a5804bbc77cefd8d778af2ded059f0e367a52930e"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _(self):
    return self.default_devel()
