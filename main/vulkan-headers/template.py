pkgname = "vulkan-headers"
pkgver = "1.3.287"
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
sha256 = "514d5e2425979ffe313b77f71274f199654b2d895719047636cb46d10555cd6b"
# no test suite
options = ["!check"]
