pkgname = "sdl3_ttf"
pkgver = "3.2.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSDLTTF_HARFBUZZ=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl3-devel", "freetype-devel", "harfbuzz-devel"]
provides = [self.with_pkgver("sdl_ttf")]
pkgdesc = "TrueType font support for SDL"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_ttf"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "ff6b81d3dc39d843cc3ead6dedd68043a79513d266792ea89445547ef4e9b073"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3_ttf-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_ttf-devel")]

    return self.default_devel()
