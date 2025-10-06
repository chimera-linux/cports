pkgname = "babl"
pkgver = "0.1.116"
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
sha256 = "50fae069867c7ade1259888ff1e3db85fec86d708252e5385b5a4f39a78ec483"
# FIXME all tests fail
hardening = ["!int"]


@subpackage("babl-devel")
def _(self):
    return self.default_devel()
