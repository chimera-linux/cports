pkgname = "libmediainfo"
pkgver = "23.07"
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
sha256 = "02748da4c6afb01651b3b65d621d7ff385b28a92472a2680b8ebfc019fd539fa"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _devel(self):
    return self.default_devel()
