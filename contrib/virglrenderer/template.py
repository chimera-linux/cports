pkgname = "virglrenderer"
pkgver = "0.10.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel", "libepoxy-devel", "mesa-devel"]
pkgdesc = "VirGL virtual OpenGL renderer"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://docs.mesa3d.org/drivers/virgl"
source = f"https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/{pkgver}/virglrenderer-{pkgver}.tar.gz"
sha256 = "da3fdc59821f645632d986482594410614a95c0c7c703b25bfb3473bd6674214"

def post_install(self):
    self.install_license("COPYING")

@subpackage("virglrenderer-devel")
def _devel(self):
    return self.default_devel()
