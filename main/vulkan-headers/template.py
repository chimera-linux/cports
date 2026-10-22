pkgname = "vulkan-headers"
pkgver = "1.4.365"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "ed832b3292cce324ebba6522fd2d3004bf1b797fa49bfbcad0b302ff23d56abc"
# no test suite
options = ["!check"]
