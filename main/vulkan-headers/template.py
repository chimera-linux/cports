pkgname = "vulkan-headers"
pkgver = "1.3.296"
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
sha256 = "e204e0b3c19f622d197df945737f5db913d6621830999b8578d34e80a7c90585"
# no test suite
options = ["!check"]
