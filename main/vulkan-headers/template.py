pkgname = "vulkan-headers"
pkgver = "1.4.334"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Vulkan header files"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/v{pkgver}.tar.gz"
)
sha256 = "f6b858ed8ff5747a32e7840ba20c565c6477c5c1c171bfc25195ef1730b349cc"
# no test suite
options = ["!check"]
