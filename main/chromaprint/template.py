pkgname = "chromaprint"
pkgver = "1.6.0"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_TOOLS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["fftw-devel", "ffmpeg-devel"]
pkgdesc = "Library that extracts fingerprints from any audio source"
license = "MIT AND LGPL-2.1-only"
url = "https://acoustid.org/chromaprint"
source = f"https://github.com/acoustid/chromaprint/releases/download/v{pkgver}/chromaprint-{pkgver}.tar.gz"
sha256 = "9d33482e56a1389a37a0d6742c376139fa43e3b8a63d29003222b93db2cb40da"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("chromaprint-devel")
def _(self):
    return self.default_devel()
