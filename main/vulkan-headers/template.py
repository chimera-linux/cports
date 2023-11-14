pkgname = "vulkan-headers"
pkgver = "1.3.270"
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
sha256 = "908e4e3881df8003744279ebdb0acd195c35d3792b2855e5488871956f90a7ee"
# no test suite
options = ["!check"]
