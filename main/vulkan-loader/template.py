pkgname = "vulkan-loader"
pkgver = "1.4.365"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DVULKAN_HEADERS_INSTALL_DIR={self.profile.sysroot / 'usr'}",
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
sha256 = "df0358f57c1936e4abd262a7327ba1f80ffb424dbbdcbcb01bb9288511f31eef"
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]


@subpackage("vulkan-loader-devel")
def _(self):
    self.depends += ["vulkan-headers"]
    return self.default_devel()
