pkgname = "vulkan-loader"
pkgver = "1.3.255"
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
sha256 = "dbce362b3279ccd3518f0d1a4c64641019390f6519a0af0f371518cb10802bfd"
# FIXME cfi
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]
