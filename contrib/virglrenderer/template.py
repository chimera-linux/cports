pkgname = "virglrenderer"
pkgver = "1.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel", "libepoxy-devel", "mesa-devel"]
pkgdesc = "VirGL virtual OpenGL renderer"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://docs.mesa3d.org/drivers/virgl"
source = f"https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/{pkgver}/virglrenderer-{pkgver}.tar.gz"
sha256 = "e4a61bfeda06e34b8df188366abff77b090fcd877536fd83db83448cdd56c72e"


def post_install(self):
    self.install_license("COPYING")


@subpackage("virglrenderer-devel")
def _devel(self):
    return self.default_devel()
