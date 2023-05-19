pkgname = "sdl_net"
pkgver = "2.2.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["sdl-devel-static"] # needs sdl_test which is static only
pkgdesc = "SDL networking library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://libsdl.org/projects/SDL_net"
source = f"{url}/release/SDL2_net-{pkgver}.tar.gz"
sha256 = "4e4a891988316271974ff4e9585ed1ef729a123d22c08bd473129179dc857feb"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("sdl_net-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
