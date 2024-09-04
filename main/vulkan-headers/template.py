pkgname = "vulkan-headers"
pkgver = "1.3.295"
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
sha256 = "b4568b984be4b8a317343cc14d854669e258705079a16cabef3fb92302f55561"
# no test suite
options = ["!check"]
