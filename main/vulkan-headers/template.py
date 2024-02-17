pkgname = "vulkan-headers"
pkgver = "1.3.278"
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
sha256 = "590cd0506be759972d0c714550c49bb90a1cc9c9e5337a10724bca6cdfd56dbe"
# no test suite
options = ["!check"]
