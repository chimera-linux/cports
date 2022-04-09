pkgname = "chromaprint"
pkgver = "1.5.1"
pkgrel = 0
build_style = "cmake"
# set to ON once ffmpeg is enabled
configure_args = ["-DBUILD_TOOLS=OFF"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
# FIXME: add back ffmpeg once compatible with 5.0
makedepends = ["fftw-devel"]
pkgdesc = "Library that extracts fingerprints from any audio source"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND LGPL-2.1-only"
url = "https://acoustid.org/chromaprint"
source = f"https://github.com/acoustid/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a1aad8fa3b8b18b78d3755b3767faff9abb67242e01b478ec9a64e190f335e1c"

def post_install(self):
    self.install_license("LICENSE.md")

@subpackage("chromaprint-devel")
def _devel(self):
    return self.default_devel()
