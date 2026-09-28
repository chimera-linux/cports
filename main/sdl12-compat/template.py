pkgname = "sdl12-compat"
pkgver = "1.2.76"
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
sha256 = "e889ac9c7e8a6bdfc31972bf1f1254b84882cb52931608bada62e8febbf0270b"


@subpackage("sdl12-compat-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
