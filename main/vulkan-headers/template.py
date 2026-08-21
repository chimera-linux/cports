pkgname = "vulkan-headers"
pkgver = "1.4.360"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "8f01247c7bbe3d1eb3fee60e19810b1503486b4342535d5e689d940b4d9414da"
# no test suite
options = ["!check"]
