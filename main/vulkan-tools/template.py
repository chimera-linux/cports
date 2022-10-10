pkgname = "vulkan-tools"
pkgver = "1.3.230"
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
sha256 = "5bb190d20ee8ae4e8dd157b686bd2d3162dc3a814b3d0625d90b1d84dd177dbb"
# no test suite
options = ["!cross", "!check"]
