pkgname = "vulkan-headers"
pkgver = "1.4.311"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "7989c360b870bcc2de52b9fd626fd2ba7a212fe177ade3aa3a10b2bcb61f8689"
# no test suite
options = ["!check"]
