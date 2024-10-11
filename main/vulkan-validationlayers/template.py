pkgname = "vulkan-validationlayers"
pkgver = "1.3.298"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/50bc4debdc3eec5045edbeb8ce164090e29b91f3.tar.gz",
    "https://github.com/martinus/robin-hood-hashing/archive/7697343363af4cc3f42cab17be49e6af9ab181e2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
    "layers/robinhood",
]
sha256 = [
    "bd9696ff425b8d0609ac40157ea2b54a6034d783f9a2d9660b130b2ba150615e",
    "19c8b75e1da7eacafa2f995709b7ed3b0cdbbc211832ab0bd2cb936b8a050ab2",
    "bce88bee05812abd863e8ae045757b66116fc9d7e880e649916d8eb71a10fa9f",
]
