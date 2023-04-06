pkgname = "vulkan-tools"
pkgver = "1.3.246"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DGLSLANG_INSTALL_DIR=/usr", "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf", "glslang-progs"]
makedepends = [
    "vulkan-headers", "vulkan-loader", "libxkbcommon-devel", "libxcb-devel",
    "libxrandr-devel", "wayland-devel", "wayland-protocols", "linux-headers",
]
pkgdesc = "Official Vulkan tools and utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
sha256 = "1aeefae204d5f750d7d46adba53bbfed5ac5b663fdefdcca57ef1bf2b8b07aef"
hardening = ["vis", "cfi"]
# no test suite
options = ["!cross", "!check"]
