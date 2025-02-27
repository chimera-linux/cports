pkgname = "sdl2_ttf"
pkgver = "2.24.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSDL2TTF_HARFBUZZ=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl2-compat-devel", "freetype-devel", "harfbuzz-devel"]
provides = [self.with_pkgver("sdl_ttf")]
pkgdesc = "TrueType font support for SDL"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_ttf"
source = f"{url}/releases/download/release-{pkgver}/SDL2_ttf-{pkgver}.tar.gz"
sha256 = "0b2bf1e7b6568adbdbc9bb924643f79d9dedafe061fa1ed687d1d9ac4e453bfd"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl2_ttf-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_ttf-devel")]

    return self.default_devel()
