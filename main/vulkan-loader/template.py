pkgname = "vulkan-loader"
pkgver = "1.3.246"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    f"-DVULKAN_HEADERS_INSTALL_DIR={self.profile().sysroot / 'usr'}",
    "-DBUILD_TESTS=OFF" # needs gtest
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = [
    "vulkan-headers", "libxcb-devel", "libxkbcommon-devel",
    "libxrandr-devel", "wayland-devel"
]
pkgdesc = "Vulkan Installable Client Driver (ICD) loader"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Loader/archive/v{pkgver}.tar.gz"
sha256 = "2531b6ef63b18040e5b0a3aa56df51e6e3cc42e7314c67a88a363be4c6975b2f"
# FIXME cfi
hardening = ["vis", "!cfi"]
# tests disabled
options = ["!check"]
