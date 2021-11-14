pkgname = "vulkan-loader"
pkgver = "1.2.182"
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
sha256 = "0d1f9fde9d21642526e9baa55d30364c95035c4fe3c6db96836631991b44dd90"
# tests disabled
options = ["!check"]
