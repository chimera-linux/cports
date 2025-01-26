pkgname = "vulkan-headers"
pkgver = "1.4.306"
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
sha256 = "18f4b4de873d071ddd7b73ea48e2ec4e7c6133e2ebb6b4236ca2345acd056994"
# no test suite
options = ["!check"]
