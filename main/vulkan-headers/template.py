pkgname = "vulkan-headers"
pkgver = "1.3.283"
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
sha256 = "a76ff77815012c76abc9811215c2167128a73a697bcc23948e858d1f7dd54a85"
# no test suite
options = ["!check"]
