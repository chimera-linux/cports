pkgname = "vulkan-validation-layers"
pkgver = "1.3.270"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_WERROR=OFF",
    "-DBUILD_WSI_WAYLAND_SUPPORT=ON",
    "-DBUILD_WSI_XCB_SUPPORT=ON",
    "-DBUILD_WSI_XLIB_SUPPORT=ON",
    "-DCMAKE_BUILD_TYPE=Release",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libx11-devel",
    "libxcb-devel",
    "libxrandr-devel",
    "robin-hood-hashing",
    "spirv-headers",
    "spirv-tools-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "vulkan-utility-libraries",
    "vulkan-utility-libraries-devel-static",
    "wayland-devel",
]
pkgdesc = "Vulkan Validation Layers"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "710bb9fc66daebe57cbab8f9fc4fe15e31068c9f9982b92a4c8e91184514a8bd"
