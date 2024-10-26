pkgname = "vulkan-validationlayers"
pkgver = "1.3.300"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://vulkan.lunarg.com/doc/sdk/latest/linux/khronos_validation_layer.html"
source = [
    f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/22c4d1b1e9d1c7d9aa5086c93e6491f21080019b.tar.gz",
    "https://github.com/martinus/robin-hood-hashing/archive/7697343363af4cc3f42cab17be49e6af9ab181e2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
    "layers/robinhood",
]
sha256 = [
    "157926f0c29e25e62e662b4101df0e8e5110e3f7f14270d8d045ff959be1546a",
    "b29082319fc523b8f25edfeacad302a4dc881904da453d2dcbb67bd040b54b29",
    "bce88bee05812abd863e8ae045757b66116fc9d7e880e649916d8eb71a10fa9f",
]
