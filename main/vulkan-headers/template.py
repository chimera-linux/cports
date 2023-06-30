pkgname = "vulkan-headers"
pkgver = "1.3.255"
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
sha256 = "8e1db7041ad6dbaf4f3326a297b4aee17f3178a0d1cf9cd76a3f934c855357b5"
# no test suite
options = ["!check"]
