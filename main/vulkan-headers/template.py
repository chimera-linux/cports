pkgname = "vulkan-headers"
pkgver = "1.3.294"
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
sha256 = "7c3844f5bd6648d5c13941941cd72b42d7f5a5dd5fbaaff546e92eb73e216b13"
# no test suite
options = ["!check"]
