pkgname = "sdl2-compat"
pkgver = "2.32.58"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl3-devel"]
# is dlopen'ed
depends = ["so:libSDL3.so.0!sdl3"]
# sdl is transitional, current names are versioned
provides = [self.with_pkgver("sdl2"), self.with_pkgver("sdl")]
pkgdesc = "Compatibility layer for SDL 2"
license = "Zlib"
url = "https://github.com/libsdl-org/sdl2-compat"
source = f"{url}/releases/download/release-{pkgver}/sdl2-compat-{pkgver}.tar.gz"
sha256 = "ae85222c007f7e2acb927c7a47c12726f56478c6f3f35ee0da1ac929f8beb53e"


@subpackage("sdl2-compat-devel-static")
def _(self):
    self.subdesc = "static libraries"

    return ["usr/lib/*.a"]


@subpackage("sdl2-compat-devel")
def _(self):
    # pull in expected makedepends for stuff
    self.depends += [self.with_pkgver("sdl2-compat-devel-static"), "sdl3-devel"]
    self.provides = [
        self.with_pkgver("sdl2-devel"),
        self.with_pkgver("sdl-devel"),
    ]

    return self.default_devel()
