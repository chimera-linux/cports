pkgname = "vulkan-headers"
pkgver = "1.3.253"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "e45a8c4289b84317252451055b0ac76b13169e10a9f619961fb6479bf6179054"
# no test suite
options = ["!check"]
