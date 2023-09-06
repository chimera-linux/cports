pkgname = "vulkan-headers"
pkgver = "1.3.263"
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
sha256 = "6a240d61965fc02b5861065dbfcd1d25418106ddb9747b99c3014faa794c2e9a"
# no test suite
options = ["!check"]
