pkgname = "vulkan-headers"
pkgver = "1.3.273"
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
sha256 = "b46c77265a0b0f235a3df755742bab273fe2083ddd52b2134e8f4c7ad3154a43"
# no test suite
options = ["!check"]
