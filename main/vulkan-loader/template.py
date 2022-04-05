pkgname = "vulkan-loader"
pkgver = "1.3.211"
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
sha256 = "1d889f093a85700f38be5d0047694c4d8c59f99e277fbe2dc781969c8f9537be"
# tests disabled
options = ["!check"]
