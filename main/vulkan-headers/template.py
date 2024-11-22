pkgname = "vulkan-headers"
pkgver = "1.3.302"
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
sha256 = "996c3f4220971e3b3cd6b8933e9e81f0bc82b6d2d6449b6f02c66946d65bf944"
# no test suite
options = ["!check"]
