pkgname = "vulkan-headers"
pkgver = "1.3.276"
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
sha256 = "91d4695fd99cc4431740e25199f540cdee23483900243e0f395e0807868589c6"
# no test suite
options = ["!check"]
