pkgname = "vulkan-loader"
pkgver = "1.3.273"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    f"-DVULKAN_HEADERS_INSTALL_DIR={self.profile().sysroot / 'usr'}",
    "-DBUILD_TESTS=OFF",  # needs gtest
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = [
    "vulkan-headers",
    "libxcb-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "wayland-devel",
]
pkgdesc = "Vulkan Installable Client Driver (ICD) loader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Loader/archive/v{pkgver}.tar.gz"
)
sha256 = "d1b7764e0fdb52f6359501ff2788d7c1c8ac7d35e9f3f4f575637bf73d1bffbd"
# FIXME cfi
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]


@subpackage("vulkan-loader-devel")
def _devel(self):
    return self.default_devel()
