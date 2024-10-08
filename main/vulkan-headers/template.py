pkgname = "vulkan-headers"
pkgver = "1.3.297"
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
sha256 = "1d679e2edc43cb7ad818b81dea960e374f1d6dd082325eb9b4c6113e76263c02"
# no test suite
options = ["!check"]
