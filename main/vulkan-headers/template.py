pkgname = "vulkan-headers"
pkgver = "1.4.326"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "19eed9a3f1e96f7fa2a30317f99374103589fba5766f9743ab61265c6889c099"
# no test suite
options = ["!check"]
