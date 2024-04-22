pkgname = "libmediainfo"
pkgver = "24.04"
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
sha256 = "5a46e68e1a09fd5b417356068bfce30ca088bd73b097efd7979b236df19c67cf"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _devel(self):
    return self.default_devel()
