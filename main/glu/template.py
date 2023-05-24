pkgname = "glu"
pkgver = "9.0.2"
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
    f"https://mesa.freedesktop.org/archive/{pkgname}/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "24effdfb952453cc00e275e1c82ca9787506aba0282145fff054498e60e19a65"


@subpackage("glu-devel")
def _devel(self):
    return self.default_devel()
