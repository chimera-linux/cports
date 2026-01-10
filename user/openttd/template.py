pkgname = "openttd"
pkgver = "15.0"
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
sha256 = "3552d774bb246f360b0a0d35436946007fcd48b2698ef1d7dfa30032ac3135c1"
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
