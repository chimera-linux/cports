pkgname = "sdl2_net"
pkgver = "2.2.0"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["sdl2-compat-devel"]
provides = [self.with_pkgver("sdl_net")]
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


@subpackage("sdl2_net-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_net-devel")]

    return self.default_devel()
