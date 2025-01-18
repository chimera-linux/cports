pkgname = "vulkan-loader"
pkgver = "1.4.305"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DVULKAN_HEADERS_INSTALL_DIR={self.profile().sysroot / 'usr'}",
    "-DBUILD_TESTS=OFF",  # needs gtest downloaded
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "gtest-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "vulkan-headers",
    "wayland-devel",
]
pkgdesc = "Vulkan Installable Client Driver (ICD) loader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Loader/archive/v{pkgver}.tar.gz"
)
sha256 = ["1f2992538ee6a9d7ff3e00fdc8dc0c3a03a6235ebb2a1b7ee2179a13bc1c5c06"]
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]


@subpackage("vulkan-loader-devel")
def _(self):
    self.depends += ["vulkan-headers"]
    return self.default_devel()
