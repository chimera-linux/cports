pkgname = "chromaprint"
pkgver = "1.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TOOLS=ON"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["fftw-devel", "ffmpeg-devel"]
pkgdesc = "Library that extracts fingerprints from any audio source"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND LGPL-2.1-only"
url = "https://acoustid.org/chromaprint"
source = f"https://github.com/acoustid/chromaprint/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a1aad8fa3b8b18b78d3755b3767faff9abb67242e01b478ec9a64e190f335e1c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("chromaprint-devel")
def _devel(self):
    return self.default_devel()
