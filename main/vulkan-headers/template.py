pkgname = "vulkan-headers"
pkgver = "1.3.298"
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
sha256 = "11681fa59966b3749776f9931972eb4748883b43a0604a9db781fbdf0983bdad"
# no test suite
options = ["!check"]
