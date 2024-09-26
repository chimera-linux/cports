pkgname = "vulkan-validationlayers"
pkgver = "1.3.296"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_WERROR=OFF",
    "-DUSE_ROBIN_HOOD_HASHING=OFF",
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
    "spirv-headers",
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/2a9b6f951c7d6b04b6c21fe1bf3f475b68b84801.tar.gz",
]
source_paths = [".", "spirv-headers"]
sha256 = [
    "99a4047b82b91b7856cbfaf2fe1629c3aa436ed2300a5e64d820b97d8c685564",
    "1698e1373bd6e59a263acef821c4d955c561b991feb6db8199833ef19ffe8a37",
]
