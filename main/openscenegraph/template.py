pkgname = "openscenegraph"
pkgver = "3.6.5"
pkgrel = 2
build_style = "cmake"
configure_args = [
    # avoid lib64
    "-DLIB_POSTFIX=",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    # no ffmpeg here, not compatible with ffmpeg 6
    "collada-dom-devel",
    "giflib-devel",
    "gst-plugins-base-devel",
    "jasper-devel",
    "curl-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "mesa-devel",
    "poppler-devel",
    "sdl2-compat-devel",
]
pkgdesc = "High-performance real-time graphics toolkit"
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
def _(self):
    return self.default_devel()
