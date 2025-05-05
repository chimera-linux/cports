pkgname = "libmediainfo"
pkgver = "25.04"
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
sha256 = "a5c5ce1e21d40c6907c47a9459c3b5f36cd5c7a0e5800f87419da10b9267becd"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _(self):
    return self.default_devel()
