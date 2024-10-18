pkgname = "vulkan-tools"
pkgver = "1.3.299"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
)
sha256 = "85f3cd64df1e7a1f06b2a660b5be55b1b2c66670100c2b28abb29436ba53e945"
# CFI: vkcube etc fail
hardening = ["vis", "!cfi"]
# no test suite
options = ["!cross", "!check"]
