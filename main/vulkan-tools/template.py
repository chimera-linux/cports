pkgname = "vulkan-tools"
pkgver = "1.3.278"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf", "glslang-progs"]
makedepends = [
    "vulkan-headers",
    "vulkan-loader-devel",
    "libxkbcommon-devel",
    "libxcb-devel",
    "libxrandr-devel",
    "volk",
    "wayland-devel",
    "wayland-protocols",
    "linux-headers",
]
pkgdesc = "Official Vulkan tools and utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
)
sha256 = "d3b18d3922b59e307597bd78c5ef260ad944767fd6d55644eec8e4971ab7517a"
# FIXME: vkcube etc fail
hardening = ["vis", "!cfi"]
# no test suite
options = ["!cross", "!check"]
