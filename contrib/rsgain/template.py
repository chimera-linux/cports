pkgname = "rsgain"
pkgver = "3.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_MANPAGE=ON"]
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
sha256 = "498f023d62898c8699b7d5da34e5e16b0e892ae8a4aec8af405f2917a82901a2"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
