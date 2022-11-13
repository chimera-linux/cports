pkgname = "vulkan-headers"
pkgver = "1.3.234"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "0bbfebd602501476e6044719619a24d8b27338fbca3ae0c69fe1daa8d0ca9caf"
# no test suite
options = ["!check"]
