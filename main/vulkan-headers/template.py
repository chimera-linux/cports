pkgname = "vulkan-headers"
pkgver = "1.3.274"
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
sha256 = "3458dd9049d561d0863069b1dd752cd4a04ca31fc090a58124691d61bff5b62a"
# no test suite
options = ["!check"]
