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
_spirv_h_pkgver = "1.4.363.0"
source = [
    f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/vulkan-sdk-{_spirv_h_pkgver}.tar.gz",
    # check scripts/known_good.json
]
source_paths = [
    ".",
    "spirv-headers",
]
sha256 = [
    "2212c1f9dd3658704929168858ff7bec0935c4e87cee5aed6b3d9735af4929ad",
    "5b3a0d099f5c7649e29c0938476c462e71d66ad89a0bde42fa1ba3eb476956c9",
]
