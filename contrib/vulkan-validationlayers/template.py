pkgname = "vulkan-validationlayers"
pkgver = "1.3.294"
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
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/f013f08e4455bcc1f0eed8e3dd5e2009682656d9.tar.gz",
]
source_paths = [".", "spirv-headers"]
sha256 = [
    "1fc7d56a04dbf1b77ef498ec9a0222fac66e1b652f1cc1800598f27b9ec28c3e",
    "452418924e8c281872e7a5ac34fdb977f2be5f880997d559e1e9062df13ae2cd",
]
