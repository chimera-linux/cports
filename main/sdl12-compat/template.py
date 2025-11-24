pkgname = "sdl12-compat"
pkgver = "1.2.70"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["glu-devel", "sdl2-compat-devel"]
# is dlopen'ed
depends = ["so:libSDL2-2.0.so.0!sdl2-compat"]
pkgdesc = "Compatibility layer for SDL 1.2"
license = "Zlib"
url = "https://github.com/libsdl-org/sdl12-compat"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "b8350cc400b9605dd5e319f451f09d5d6e70bb1dfc22cd67f718b3ffc16ebb7c"


@subpackage("sdl12-compat-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
