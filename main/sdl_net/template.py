pkgname = "sdl_net"
pkgver = "2.0.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["sdl-devel"]
pkgdesc = "SDL networking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libsdl.org/projects/SDL_net"
source = f"{url}/release/SDL2_net-{pkgver}.tar.gz"
sha256 = "15ce8a7e5a23dafe8177c8df6e6c79b6749a03fff1e8196742d3571657609d21"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("COPYING.txt")

@subpackage("sdl_net-static")
def _static(self):
    return self.default_static()

@subpackage("sdl_net-devel")
def _devel(self):
    return self.default_devel()
