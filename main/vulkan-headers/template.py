pkgname = "vulkan-headers"
pkgver = "1.4.304"
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
sha256 = "5e1a06b3f27e7581b55d1dea176fd97ee0a2f299406db2f437c1d2f297ceba5b"
# no test suite
options = ["!check"]
