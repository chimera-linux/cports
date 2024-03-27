pkgname = "openscenegraph"
pkgver = "3.6.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # avoid lib64
    "-DLIB_POSTFIX="
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    # no ffmpeg here, not compatible with ffmpeg 6
    "mesa-devel",
    "libcurl-devel",
    "giflib-devel",
    "librsvg-devel",
    "jasper-devel",
    "libtiff-devel",
    "sdl-devel",
    "gst-plugins-base-devel",
    "libpoppler-devel",
    "libxrandr-devel",
    "libxinerama-devel",
]
pkgdesc = "High-performance real-time graphics toolkit"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:OpenSceneGraph"
url = "https://openscenegraph.com"
source = f"https://github.com/openscenegraph/OpenSceneGraph/archive/OpenSceneGraph-{pkgver}.tar.gz"
sha256 = "aea196550f02974d6d09291c5d83b51ca6a03b3767e234a8c0e21322927d1e12"
# unit tests are off
options = ["!check", "!cross"]


def post_install(self):
    self.install_file("CMakeModules/FindOSG.cmake", "usr/lib/cmake/OSG")
    self.install_license("LICENSE.txt")


@subpackage("openscenegraph-devel")
def _devel(self):
    return self.default_devel()
