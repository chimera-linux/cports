pkgname = "vulkan-headers"
pkgver = "1.3.211"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "67ab69142f69389dfdf5f1c7922e62aa4a03ba286b9229dd7f7f3e827232463c"
# no test suite
options = ["!check"]
