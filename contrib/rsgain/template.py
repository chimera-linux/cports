pkgname = "rsgain"
pkgver = "3.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "fmt-devel",
    "inih-devel",
    "libebur128-devel",
    "taglib-devel",
    "zlib-devel",
]
pkgdesc = "ReplayGain 2.0 tagging utility"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/complexlogic/rsgain"
source = f"{url}/releases/download/v{pkgver}/rsgain-{pkgver}-source.tar.xz"
sha256 = "e1eb7993b8aafad1d57df90ed92ec4c902884933976e914048a87708d98fb37c"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
