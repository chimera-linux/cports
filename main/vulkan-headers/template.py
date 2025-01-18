pkgname = "vulkan-headers"
pkgver = "1.4.305"
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
sha256 = "7581c5ed0337ffeef0707651561f722700081bc69c62c582c470cd77c2be0920"
# no test suite
options = ["!check"]
