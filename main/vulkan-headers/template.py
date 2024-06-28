pkgname = "vulkan-headers"
pkgver = "1.3.289"
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
sha256 = "fc66db6de66a6e3527c110ff1db77a86ae97804fe7f019725e8d25acdc875c6f"
# no test suite
options = ["!check"]
