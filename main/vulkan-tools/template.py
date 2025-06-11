pkgname = "vulkan-tools"
pkgver = "1.4.317"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = [
    "cmake",
    "glslang-progs",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "libxcb-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "linux-headers",
    "volk",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Official Vulkan tools and utilities"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
)
sha256 = "4586309ab5b2a9584fde62fd85b0ef5bb98b4cdbca9cb1ba3a2b4978dc2f355c"
# CFI: vkcube etc fail
hardening = ["vis", "!cfi"]
# no test suite
options = ["!cross", "!check"]
