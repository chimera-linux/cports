pkgname = "vulkan-headers"
pkgver = "1.3.268"
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
sha256 = "d5c59d5fc3ab264006dfea1eb1a11f609ea5dfa8319a5aaca061007828012a78"
# no test suite
options = ["!check"]
