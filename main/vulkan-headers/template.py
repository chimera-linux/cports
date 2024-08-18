pkgname = "vulkan-headers"
pkgver = "1.3.293"
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
sha256 = "2d7ca5577e5b94d1023b89ad28e8eda387a3488abdbb876f0177353f968d4ad1"
# no test suite
options = ["!check"]
