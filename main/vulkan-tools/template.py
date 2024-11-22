pkgname = "vulkan-tools"
pkgver = "1.3.302"
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
sha256 = "75264092f597e883c236345f188d4f09b635891fba53b517d9953aff8ada6571"
# CFI: vkcube etc fail
hardening = ["vis", "!cfi"]
# no test suite
options = ["!cross", "!check"]
