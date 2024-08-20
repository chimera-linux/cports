pkgname = "mgba"
pkgver = "0.10.3"
pkgrel = 1
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
sha256 = "be2cda7de3da8819fdab0c659c5cd4c4b8ca89d9ecddeeeef522db6d31a64143"
hardening = ["!int"]


@subpackage("mgba-devel")
def _(self):
    return self.default_devel()
