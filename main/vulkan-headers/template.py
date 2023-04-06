pkgname = "vulkan-headers"
pkgver = "1.3.246"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "4fb971a152d4f02878a779d643cc86c66a0455ce23fdfa1404ce112eb8f718a5"
# no test suite
options = ["!check"]
