pkgname = "vulkan-headers"
pkgver = "1.3.243"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
sha256 = "76c57490740369a26d68dd26d308e2faa2e0fc5d255498aa48ee389534fc5a48"
# no test suite
options = ["!check"]
