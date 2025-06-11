pkgname = "vulkan-headers"
pkgver = "1.4.317"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "78665959d10b09061d8c3e21db8bf3e8b699e2d3d532fce850a32312dba7228b"
# no test suite
options = ["!check"]
