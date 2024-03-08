pkgname = "vulkan-headers"
pkgver = "1.3.280"
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
sha256 = "717b49c52dbd37c78cf2f7f0fc715292c42e74841219e6cca918cd293ad5dce4"
# no test suite
options = ["!check"]
