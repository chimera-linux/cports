pkgname = "sdl_gpu"
pkgver = "0.12.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUSE_SYSTEM_GLEW=YES"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["glew-devel", "sdl-devel"]
pkgdesc = "Library for high-performance 2D graphics with SDL"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/grimfang4/sdl-gpu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "00b7dd7fe30cdc95483c2ad5de347855d4e984bd5e8da56f3c24a4a2960fc9ba"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl_gpu-devel")
def _devel(self):
    self.depends = ["glew-devel", "sdl-devel"]
    return self.default_devel()
