pkgname = "vulkan-headers"
pkgver = "1.3.284"
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
sha256 = "141619d4ce53814802a9311112902a95749ba16b32c0ee7997335c4988689686"
# no test suite
options = ["!check"]
