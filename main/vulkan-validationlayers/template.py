pkgname = "vulkan-validationlayers"
pkgver = "1.4.317"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DBUILD_WERROR=OFF",
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/c9aad99f9276817f18f72a4696239237c83cb775.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "c8af30a15d273ed68f2314cff1c0d506b30958b4e08bdfc3daff2e917043b951",
    "733993f563ab36b3f3f6ef155caf792e37c4768290fcc23456126241b2b53829",
]
