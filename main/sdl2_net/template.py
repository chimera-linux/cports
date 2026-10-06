pkgname = "sdl2_net"
pkgver = "2.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["sdl2-compat-devel"]
provides = [self.with_pkgver("sdl_net")]
pkgdesc = "SDL networking library"
license = "BSD-3-Clause"
url = "https://libsdl.org/projects/SDL_net"
source = f"{url}/release/SDL2_net-{pkgver}.tar.gz"
sha256 = "9cbca2527feb3f1a622d48ba65cc7dee9b1e3f2c55ceafb7d7720bb058aafb30"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl2_net-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_net-devel")]

    return self.default_devel()
