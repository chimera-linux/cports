pkgname = "embree"
pkgver = "4.3.1"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release", "-DEMBREE_TUTORIALS=OFF"]
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "glfw-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "mesa-devel",
    "onetbb-devel",
    "openimageio-devel",
]
pkgdesc = "Ray tracing library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://www.embree.org"
source = f"https://github.com/embree/embree/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "824edcbb7a8cd393c5bdb7a16738487b21ecc4e1d004ac9f761e934f97bb02a4"


@subpackage("embree-devel")
def _devel(self):
    return self.default_devel()
