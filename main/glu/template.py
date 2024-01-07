pkgname = "glu"
pkgver = "9.0.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgl_provider=gl"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["mesa-devel"]
pkgdesc = "Mesa OpenGL utility library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "SGI-B-2.0"
url = "https://gitlab.freedesktop.org/mesa/glu"
source = (
    f"https://mesa.freedesktop.org/archive/{pkgname}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "bd43fe12f374b1192eb15fe20e45ff456b9bc26ab57f0eee919f96ca0f8a330f"


@subpackage("glu-devel")
def _devel(self):
    return self.default_devel()
