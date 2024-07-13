pkgname = "vulkan-headers"
pkgver = "1.3.290"
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
sha256 = "c4606a201e8704d75bb974657f08604013d073a862cc127f9f31760213f3afa0"
# no test suite
options = ["!check"]
