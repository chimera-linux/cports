pkgname = "vulkan-validationlayers"
pkgver = "1.4.350"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/ad9184e76a66b1001c29db9b0a3e87f646c64de0.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "4fb9f0c72d840d2d2afd7b085891cd8ec1e74f8f3667d7683910890716e112ca",
    "b5b7eba62453eb8c6f6a5fbf7155b71cde693bafe9cd5f03b79ed8c714816afe",
]
