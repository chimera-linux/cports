pkgname = "libgme"
pkgver = "0.6.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_UBSAN=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "sdl2-compat-devel"]
pkgdesc = "Video game music file emulation/playback library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://bitbucket.org/mpyne/game-music-emu/wiki/Home"
source = f"https://bitbucket.org/mpyne/game-music-emu/downloads/game-music-emu-{pkgver}.tar.xz"
sha256 = "aba34e53ef0ec6a34b58b84e28bf8cfbccee6585cebca25333604c35db3e051d"
hardening = ["!vis", "!cfi"]
# no test target
options = ["!check"]

if self.profile().endian == "big":
    tool_flags = {"CXXFLAGS": ["-DMSB_FIRST=1"]}
else:
    tool_flags = {"CXXFLAGS": ["-DLSB_FIRST=1"]}


@subpackage("libgme-devel")
def _(self):
    return self.default_devel()
