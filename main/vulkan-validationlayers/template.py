pkgname = "vulkan-validationlayers"
pkgver = "1.4.334"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/f2e4bd213104fe323a01e935df56557328d37ac8.tar.gz",
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "8a730695f9e0181febf66847181c14830d2f7d64cb32006fb9e273a1bb86b76c",
    "4e26fecd4142ca178df6b8f24485d2215ef0621de534cd277faeb33d3e06d897",
]
