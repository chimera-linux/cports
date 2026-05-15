pkgname = "libmediainfo"
pkgver = "26.01"
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
sha256 = "173947f0274babf090ba508f35c5551069296609b02bf3659e41958d8b9c2a1e"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _(self):
    return self.default_devel()
