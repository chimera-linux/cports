pkgname = "rsgain"
pkgver = "3.6"
pkgrel = 1
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
sha256 = "26d46f1240a83366e82cbc9121a467fc1dcc977c7adfb4e15c99ead6b3d07ec8"


def post_install(self):
    self.install_license("LICENSE")
