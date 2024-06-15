pkgname = "vulkan-headers"
pkgver = "1.3.288"
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
sha256 = "6f21dd9efe65fb7aeba6beaef2d274a0a31d32b4f494637b0d1a49853cf20ca6"
# no test suite
options = ["!check"]
