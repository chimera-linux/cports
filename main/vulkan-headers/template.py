pkgname = "vulkan-headers"
pkgver = "1.2.199"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "c4b860e267312364aa0b36e457e5ac8c114fe0957f216668c9da9211ef4643d0"
# no test suite
options = ["!check"]
