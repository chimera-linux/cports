pkgname = "mgba"
pkgver = "0.10.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "libzip-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "elfutils-devel",
    "ffmpeg-devel",
    "libedit-devel",
    "libepoxy-devel",
    "libpng-devel",
    "libzip-devel",
    "lua5.4-devel",
    "minizip-devel",
    # next release: qt6
    "sdl-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "GBA emulator"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MPL-2.0"
url = "https://mgba.io"
source = f"https://github.com/mgba-emu/mgba/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f85eeb8f78f847f5217a87bd5e2d6c1214b461ffd4ec129cc656162ab707cb24"
hardening = ["!int"]


@subpackage("mgba-devel")
def _(self):
    return self.default_devel()
