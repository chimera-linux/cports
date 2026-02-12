pkgname = "openttd"
pkgver = "15.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "curl-devel",
    "fluidsynth-devel",
    "fontconfig-devel",
    "freetype-devel",
    "harfbuzz-devel",
    "icu-devel",
    "libpng-devel",
    "lzo-devel",
    "sdl2-compat-devel",
    "xz-devel",
    "zlib-ng-devel",
]
pkgdesc = "Simulation game based upon Transport Tycoon Deluxe"
license = "GPL-2.0-or-later"
url = "https://openttd.org"
source = f"https://cdn.openttd.org/openttd-releases/{pkgver}/openttd-{pkgver}-source.tar.xz"
sha256 = "22466afe047ca2b77f18e7d4890d3b38f1c1b27f15c795ec20cc1e7045a9b169"
# SetBitIterator tests (src/tests/bitmath_func.cpp) fail with int enabled (and the game crashes when the tests are skipped)
hardening = ["!int"]
# can't cross compile due to https://github.com/OpenTTD/OpenTTD/issues/8249
options = ["!cross"]


def check(self):
    self.do("./build/openttd_test")


@subpackage("openttd-locale")
def _(self):
    self.install_if = [self.parent, "base-locale"]
    return ["usr/share/games/openttd/lang/*[!english]*.lng"]
