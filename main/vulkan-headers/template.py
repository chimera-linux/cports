pkgname = "vulkan-headers"
pkgver = "1.3.225"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "71bfa18ef3df0c39b1dc194727166e4ec1c51df7254ac86e0b9c27fd10cf85ad"
# no test suite
options = ["!check"]
