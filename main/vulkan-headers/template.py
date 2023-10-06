pkgname = "vulkan-headers"
pkgver = "1.3.267"
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
sha256 = "72120553215bb631275a38a5359ad812837165ab8ddd8e33597dd52c7d80d627"
# no test suite
options = ["!check"]
