pkgname = "vulkan-headers"
pkgver = "1.3.252"
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
sha256 = "2262a7ba3e12583a5f5f7ebac0c01003cf106baf0ea75809e07958fa9334ea49"
# no test suite
options = ["!check"]
