pkgname = "vulkan-headers"
pkgver = "1.4.303"
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
sha256 = "fdf0e2e05356b455137ff97f837c9689ba253ec7d20f87ad81575b9bdbe7fdd4"
# no test suite
options = ["!check"]
