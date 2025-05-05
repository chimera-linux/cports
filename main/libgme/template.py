pkgname = "libgme"
pkgver = "0.6.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_UBSAN=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-ng-compat-devel", "sdl2-compat-devel"]
pkgdesc = "Video game music file emulation/playback library"
license = "LGPL-2.1-or-later"
url = "https://github.com/libgme/game-music-emu"
source = f"{url}/releases/download/{pkgver}/libgme-{pkgver}-src.tar.gz"
sha256 = "6f94eac735d86bca998a7ce1170d007995191ef6d4388345a0dc5ffa1de0bafa"
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
