pkgname = "virglrenderer"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel", "libepoxy-devel", "mesa-devel"]
pkgdesc = "VirGL virtual OpenGL renderer"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://docs.mesa3d.org/drivers/virgl"
source = f"https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/{pkgver}/virglrenderer-{pkgver}.tar.gz"
sha256 = "130c417bfcc8d35063245322609fd310e981a33e2a6c73beac7fb98c4beed8e6"


def post_install(self):
    self.install_license("COPYING")


@subpackage("virglrenderer-devel")
def _devel(self):
    return self.default_devel()
