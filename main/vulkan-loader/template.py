pkgname = "vulkan-loader"
pkgver = "1.4.326"
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
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Loader/archive/v{pkgver}.tar.gz"
)
sha256 = "86772b60eeef6f510586636b7cf7a0e0eabd9e9920bcabf6e8f3b1c2a634a4cc"
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]


@subpackage("vulkan-loader-devel")
def _(self):
    self.depends += ["vulkan-headers"]
    return self.default_devel()
