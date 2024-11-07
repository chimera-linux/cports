pkgname = "vulkan-headers"
pkgver = "1.3.301"
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
sha256 = "6c02949bed7f3984e1d12263bdce52a1c99e54a1abcdae90d00527c2890c1cc5"
# no test suite
options = ["!check"]
