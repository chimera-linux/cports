pkgname = "virglrenderer"
pkgver = "1.1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel", "libepoxy-devel", "mesa-devel"]
pkgdesc = "VirGL virtual OpenGL renderer"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://docs.mesa3d.org/drivers/virgl"
source = f"https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/{pkgver}/virglrenderer-{pkgver}.tar.gz"
sha256 = "9996b87bda2fbf515473b60f32b00ed58847da733b47053923fd2cb035a6f5a2"


def post_install(self):
    self.install_license("COPYING")


@subpackage("virglrenderer-devel")
def _(self):
    return self.default_devel()
