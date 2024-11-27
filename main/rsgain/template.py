pkgname = "rsgain"
pkgver = "3.5.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DINSTALL_MANPAGE=ON",
    "-DUSE_STD_FORMAT=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "inih-devel",
    "libebur128-devel",
    "taglib-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "ReplayGain 2.0 tagging utility"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/complexlogic/rsgain"
source = f"{url}/releases/download/v{pkgver}/rsgain-{pkgver}-source.tar.xz"
sha256 = "3626e7adaee475be3c72c78cd1e8c6ffa38062daf48c8e8a8591c16022ff6bf4"


def post_install(self):
    self.install_license("LICENSE")
