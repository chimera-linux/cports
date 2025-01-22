pkgname = "sdl2_ttf"
pkgver = "2.22.0"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DSDL2TTF_HARFBUZZ=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl2-compat-devel", "freetype-devel", "harfbuzz-devel"]
provides = [self.with_pkgver("sdl_ttf")]
pkgdesc = "TrueType font support for SDL"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_ttf"
source = f"{url}/releases/download/release-{pkgver}/SDL2_ttf-{pkgver}.tar.gz"
sha256 = "d48cbd1ce475b9e178206bf3b72d56b66d84d44f64ac05803328396234d67723"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl2_ttf-devel")
def _(self):
    self.provides = [self.with_pkgver("sdl_ttf-devel")]

    return self.default_devel()
