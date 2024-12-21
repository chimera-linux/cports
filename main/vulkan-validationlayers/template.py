pkgname = "vulkan-validationlayers"
pkgver = "1.4.304"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_WERROR=OFF",
    "-DUSE_ROBIN_HOOD_HASHING=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libx11-devel",
    "libxcb-devel",
    "libxrandr-devel",
    "spirv-tools-devel",
    "vulkan-headers",
    "vulkan-utility-libraries",
    "wayland-devel",
]
pkgdesc = "Validation layers to catch Vulkan issues"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://vulkan.lunarg.com/doc/sdk/latest/linux/khronos_validation_layer.html"
source = [
    f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/3f17b2af6784bfa2c5aa5dbb8e0e74a607dd8b3b.tar.gz",
    "https://github.com/martinus/robin-hood-hashing/archive/7697343363af4cc3f42cab17be49e6af9ab181e2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
    "layers/robinhood",
]
sha256 = [
    "fd889b0135b7770a3d9819ed1273009ddd654b9715b09c0af150eca8ffc15eb2",
    "2301e11e5c77213258d6863bf4e6c607a8c6431fa8336e98ac6a2131bd6284f8",
    "bce88bee05812abd863e8ae045757b66116fc9d7e880e649916d8eb71a10fa9f",
]
