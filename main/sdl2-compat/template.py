pkgname = "sdl2-compat"
pkgver = "2.30.50"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl3-devel", "sdl3-devel-static"]  # needs libSDL3_test.a
# is dlopen'ed
depends = ["so:libSDL3.so.0!sdl"]
# manually cap provided version so this isn't prioritized over main/sdl
provides = ["so:libSDL2-2.0.so.0=0"]
pkgdesc = "Compatibility layer for SDL 2"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/libsdl-org/sdl2-compat"
source = f"{url}/releases/download/release-{pkgver}/sdl2-compat-{pkgver}.tar.gz"
sha256 = "f65e369b45c4cf2981f446541b1754ccb4714a7ec62fad339d75c0176b8fa212"


@subpackage("sdl2-compat-devel")
def _(self):
    # see above
    self.provides = [
        "cmd:sdl2-config=2.30.0",
        "pc:sdl2=2.30.0",
    ]

    return self.default_devel()
