pkgname = "vulkan-headers"
pkgver = "1.3.275"
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
sha256 = "7161da645dbd33fd4ea61eec08e0d77389a640010acbf4afc00234f84df9b314"
# no test suite
options = ["!check"]
