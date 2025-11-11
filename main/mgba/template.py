pkgname = "mgba"
pkgver = "0.10.5"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
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
    "sdl2-compat-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "GBA emulator"
license = "MPL-2.0"
url = "https://mgba.io"
source = f"https://github.com/mgba-emu/mgba/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "91d6fbd32abcbdf030d58d3f562de25ebbc9d56040d513ff8e5c19bee9dacf14"
hardening = ["!int"]


@subpackage("mgba-devel")
def _(self):
    return self.default_devel()
