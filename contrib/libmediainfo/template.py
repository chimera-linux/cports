pkgname = "libmediainfo"
pkgver = "24.06"
pkgrel = 0
build_wrksrc = "Project/CMake"
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["pkgconf", "cmake", "ninja"]
makedepends = [
    "libcurl-devel",
    "libmms-devel",
    "libzen-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Shared library for mediainfo"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/libmediainfo/{pkgver}/libmediainfo_{pkgver}.tar.bz2"
sha256 = "891b471497eb3e6a1e8f7557fcf039b62b1ec71ef2e647695ddf92290dd2a1d8"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _(self):
    return self.default_devel()
