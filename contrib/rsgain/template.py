pkgname = "rsgain"
pkgver = "3.4"
pkgrel = 1
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
sha256 = "392ad1407eea7737c6f63b6a0681a3df51f33033d2d16b644f407e6ef3f28013"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
