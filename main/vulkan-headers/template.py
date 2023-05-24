pkgname = "vulkan-headers"
pkgver = "1.3.247"
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
sha256 = "4c5c99bd64b5f74bdaec012e69dd5567deb52d78f12f6d2c43c29fd0a1eee87e"
# no test suite
options = ["!check"]
