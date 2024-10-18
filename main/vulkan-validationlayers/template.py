pkgname = "vulkan-validationlayers"
pkgver = "1.3.299"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/252dc2df08f58e0e50c8437edc0e77eacdfb7559.tar.gz",
    "https://github.com/martinus/robin-hood-hashing/archive/7697343363af4cc3f42cab17be49e6af9ab181e2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
    "layers/robinhood",
]
sha256 = [
    "90401df60bb6e540d22510dad95d616c9a5a92db64d9db7a177f78d643c56d10",
    "e32831eb66e6425455b588ce5b91a20abf20bd4c794436b0b4d48b3b0b9a2971",
    "bce88bee05812abd863e8ae045757b66116fc9d7e880e649916d8eb71a10fa9f",
]
