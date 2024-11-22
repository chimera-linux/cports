pkgname = "vulkan-loader"
pkgver = "1.3.302"
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
sha256 = ["7f8d3e5c7428fe2d6220a4ea1c0270c7695bfef8e48c38b827e9e81880637710"]
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]


@subpackage("vulkan-loader-devel")
def _(self):
    self.depends += ["vulkan-headers"]
    return self.default_devel()
