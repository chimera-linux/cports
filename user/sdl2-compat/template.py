pkgname = "sdl2-compat"
_commit = "fbbb14acca6fa630fb955856dbeb5b0e0a1c93b8"
pkgver = "0_git20250106"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl3-devel-static"]  # needs libSDL3_test.a
# is dlopen'ed
depends = ["so:libSDL3.so.0!sdl"]
# manually cap provided version so this isn't prioritized over main/sdl
provides = ["so:libSDL2-2.0.so.0=0"]
pkgdesc = "Compatibility layer for SDL 2"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/libsdl-org/sdl2-compat"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "20a7844be9f284a15039500cfd66302090fd3e8be3e4d3b60050d5fa191b820d"


@subpackage("sdl2-compat-devel")
def _(self):
    # see above
    self.provides = [
        "cmd:sdl2-config=2",
        "pc:sdl2=2",
    ]

    return self.default_devel()
