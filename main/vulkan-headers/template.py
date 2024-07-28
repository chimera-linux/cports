pkgname = "vulkan-headers"
pkgver = "1.3.292"
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
sha256 = "1e64b66ac0063f2192db7b7443d9d732b656614a3e4b76c58697e98a26fc245d"
# no test suite
options = ["!check"]
