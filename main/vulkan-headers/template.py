pkgname = "vulkan-headers"
pkgver = "1.3.299"
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
sha256 = "95bb8fe731469b9e1be532b9d3b4d7d33e28ddbd99a926da7f0eca82a134b92f"
# no test suite
options = ["!check"]
