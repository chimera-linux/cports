pkgname = "vulkan-headers"
pkgver = "1.3.269"
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
sha256 = "1637f36a023bd148315f66efb7974861adf22cd1f6d690bdf00ee15ce91d5367"
# no test suite
options = ["!check"]
