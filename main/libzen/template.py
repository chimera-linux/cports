pkgname = "libzen"
pkgver = "0.4.41"
pkgrel = 0
build_wrksrc = "Project/CMake"
build_style = "cmake"
hostmakedepends = ["pkgconf", "cmake", "ninja"]
pkgdesc = "Shared library for libmediainfo and mediainfo"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/libzen/{pkgver}/libzen_{pkgver}.tar.bz2"
sha256 = "eb237d7d3dca6dc6ba068719420a27de0934a783ccaeb2867562b35af3901e2d"


@subpackage("libzen-devel")
def _(self):
    return self.default_devel()
