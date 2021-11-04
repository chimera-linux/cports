pkgname = "vulkan-headers"
pkgver = "1.2.182"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "38d1c953de7bb2d839556226851feeb690f0d23bc22ac46c823dcb66c97bfdc8"
# no test suite
options = ["!check"]
