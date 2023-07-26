pkgname = "vulkan-headers"
pkgver = "1.3.259"
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
sha256 = "da9e625935014e8aa1c31c4ab45d7b015d73185586b1bdf70c646d66cbddc3d3"
# no test suite
options = ["!check"]
