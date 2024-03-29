pkgname = "libmediainfo"
pkgver = "24.03"
pkgrel = 0
build_wrksrc = "Project/CMake"
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["pkgconf", "cmake", "ninja"]
makedepends = ["libcurl-devel", "libzen-devel", "libmms-devel", "zlib-devel"]
pkgdesc = "Shared library for mediainfo"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/libmediainfo/{pkgver}/libmediainfo_{pkgver}.tar.bz2"
sha256 = "381226fc13495f3e7f12365aa83acbdd142b4c7b12d0c31314d871c85b204a16"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _devel(self):
    return self.default_devel()
