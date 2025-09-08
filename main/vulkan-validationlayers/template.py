pkgname = "vulkan-validationlayers"
pkgver = "1.4.326"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/e6d5e88c07cc66a798b668945e7fb29ec1cfee27.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "41b0a3d5b8a0a1ed395650adfc453b9711ee02c27abdc27845dc58c683d31268",
    "fac301cb7156dbe747fa6fc6700a8a9265519c0d15a592884cc1515cc2852c9f",
]
