pkgname = "libmediainfo"
pkgver = "25.07"
pkgrel = 0
build_wrksrc = "Project/CMake"
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["pkgconf", "cmake", "ninja"]
makedepends = [
    "curl-devel",
    "libmms-devel",
    "libzen-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Shared library for mediainfo"
license = "BSD-2-Clause"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/libmediainfo/{pkgver}/libmediainfo_{pkgver}.tar.bz2"
sha256 = "1d03caaf979128dc62e49737882d076e83440f44c048d84458a131e6d4e070dd"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _(self):
    return self.default_devel()
