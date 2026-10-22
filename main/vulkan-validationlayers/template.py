pkgname = "vulkan-validationlayers"
pkgver = "1.4.365"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_WERROR=OFF",
    "-DUPDATE_DEPS=OFF",
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
license = "Apache-2.0"
url = "https://vulkan.lunarg.com/doc/sdk/latest/linux/khronos_validation_layer.html"
source = [
    f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/v{pkgver}.tar.gz",
    # check scripts/known_good.json
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/496543121ce6419f23d6fa5d7194ba66c36212d2.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "2212c1f9dd3658704929168858ff7bec0935c4e87cee5aed6b3d9735af4929ad",
    "a9bb9c48713245eacf97cc539b6f1d45405a92d8813f8b82e635f0a085ee9898",
]
