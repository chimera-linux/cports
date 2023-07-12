pkgname = "vulkan-headers"
pkgver = "1.3.257"
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
sha256 = "e3ee02eff07ebcdb0ddfd06366d986c889f3392b6c4d79615bb06aefc1fda900"
# no test suite
options = ["!check"]
