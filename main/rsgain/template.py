pkgname = "rsgain"
pkgver = "3.8"
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
license = "BSD-2-Clause"
url = "https://github.com/complexlogic/rsgain"
source = f"{url}/releases/download/v{pkgver}/rsgain-{pkgver}-source.tar.xz"
sha256 = "0c590fa8ecd084e181dca6d4776f29d532d36c53cb8fde56f87f1270ce45a3cd"


def post_install(self):
    self.install_license("LICENSE")
