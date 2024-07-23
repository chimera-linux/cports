pkgname = "vulkan-headers"
pkgver = "1.3.291"
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
sha256 = "69a41e5d6c5def1b85dc62ddbdcd03f5ef4de3691192dfc97c12bfcf3983e8ff"
# no test suite
options = ["!check"]
