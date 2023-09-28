pkgname = "vulkan-headers"
pkgver = "1.3.266"
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
sha256 = "0b3451c3dbda492be010738fb90e5cf80aa32f66705cadd9a12c573e0e351fd3"
# no test suite
options = ["!check"]
