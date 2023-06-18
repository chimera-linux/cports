pkgname = "vulkan-headers"
pkgver = "1.3.254"
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
sha256 = "6be000a33b665ecac05971819b4c29ba5e21b800627f288f4d3a0b28e86b290f"
# no test suite
options = ["!check"]
