pkgname = "vulkan-validationlayers"
pkgver = "1.4.360"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/29981f65241605e08b0ede4cfeb999fe3b723c6a.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "550c5ff6a8fd7859726fd3c5fdc5b75a774fcddc5db209c15227fbd92e34c824",
    "232899f1ad4104fb5bc377b94596c7621575eee62ad9a9e8f929b63a7dd8a7ad",
]
