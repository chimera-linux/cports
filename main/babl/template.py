pkgname = "babl"
pkgver = "0.1.114"
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
sha256 = "bcbb7786c1e447703db3bc7fa34d62d0d2d117b22f04d8834c7b2d5ded456487"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _(self):
    return self.default_devel()
