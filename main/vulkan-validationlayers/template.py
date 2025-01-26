pkgname = "vulkan-validationlayers"
pkgver = "1.4.306"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/2b2e05e088841c63c0b6fd4c9fb380d8688738d3.tar.gz",
    "https://github.com/martinus/robin-hood-hashing/archive/7697343363af4cc3f42cab17be49e6af9ab181e2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
    "layers/robinhood",
]
sha256 = [
    "9756a34e206e8d1fff4dfb951d46536ab2eb14e12bcdafbb79202155ec48c1a9",
    "2e226ee953472e2e39724bf315433dce8cf119a397c451742dfda25bab7690af",
    "bce88bee05812abd863e8ae045757b66116fc9d7e880e649916d8eb71a10fa9f",
]
