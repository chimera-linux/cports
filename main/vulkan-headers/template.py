pkgname = "vulkan-headers"
pkgver = "1.3.272"
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
sha256 = "e59bd50ac9f5f5df635a721f828245668fb7af07878cc9d170996a3a83b44560"
# no test suite
options = ["!check"]
