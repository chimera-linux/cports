pkgname = "vulkan-headers"
pkgver = "1.3.227"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "5b345a9f0dafc96e4d0cd2d95547702c4451691dc731f6b486ba36fd9bab7bfe"
# no test suite
options = ["!check"]
