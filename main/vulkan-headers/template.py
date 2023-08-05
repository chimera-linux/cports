pkgname = "vulkan-headers"
pkgver = "1.3.261"
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
sha256 = "0c67b2b76a7d6534c0f98085dbbcd4a1ac945b15b269bc81ee7dbe6cf28d53bb"
# no test suite
options = ["!check"]
