pkgname = "sdl12-compat"
pkgver = "1.2.68"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["glu-devel", "sdl2-compat-devel"]
# is dlopen'ed
depends = ["so:libSDL2-2.0.so.0!sdl"]
pkgdesc = "Compatibility layer for SDL 1.2"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/libsdl-org/sdl12-compat"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "63c6e4dcc1154299e6f363c872900be7f3dcb3e42b9f8f57e05442ec3d89d02d"


@subpackage("sdl12-compat-devel")
def _(self):
    self.depends += makedepends

    return self.default_devel()
