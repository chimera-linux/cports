pkgname = "rsgain"
pkgver = "3.5.2"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/complexlogic/rsgain"
source = f"{url}/releases/download/v{pkgver}/rsgain-{pkgver}-source.tar.xz"
sha256 = "4f701521fd270b60f536a12aeb64e09bb87f24c30d576231d2fda3b6cc8c697e"


def post_install(self):
    self.install_license("LICENSE")
