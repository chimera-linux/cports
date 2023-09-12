pkgname = "vulkan-headers"
pkgver = "1.3.264"
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
sha256 = "bdce6a99f0e5869a341946ee0a92eef270ef9b4b106e82f238aa68aeb2cd4995"
# no test suite
options = ["!check"]
