pkgname = "vulkan-headers"
pkgver = "1.3.285"
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
sha256 = "212455eeab2cef5d93b1b991e548afe184f294428118f747989a97677e19ab2a"
# no test suite
options = ["!check"]
