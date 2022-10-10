pkgname = "vulkan-headers"
pkgver = "1.3.230"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "7ffa5489eb64c11449ebc63579cbbd3bf6d8144cdd96434033f837c2b615847d"
# no test suite
options = ["!check"]
