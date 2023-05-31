pkgname = "vulkan-headers"
pkgver = "1.3.251"
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
sha256 = "e14ac3a6868d9cffcd76e8e92eb0373eb675ab5725672af35b4ba664348e8261"
# no test suite
options = ["!check"]
