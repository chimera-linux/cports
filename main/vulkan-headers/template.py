pkgname = "vulkan-headers"
pkgver = "1.3.300"
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
sha256 = "9a0542fb2233e39179fcc9aba8b0dd9deee4a19a2d7adb89449144b2e3d80e93"
# no test suite
options = ["!check"]
