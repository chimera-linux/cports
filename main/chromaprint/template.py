pkgname = "chromaprint"
pkgver = "1.6.1"
pkgrel = 0
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
sha256 = "3368805af0ee47b9df74df10b5001a44569e01df2844dab520031720dde9ad23"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("chromaprint-devel")
def _(self):
    return self.default_devel()
