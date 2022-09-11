pkgname = "vulkan-validationlayers"
pkgver = "1.3.227"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DSPIRV_HEADERS_INSTALL_DIR=/usr",
    "-DGLSLANG_INSTALL_DIR=/usr",
    "-DBUILD_LAYER_SUPPORT_FILES=ON",
    "-DUSE_ROBIN_HOOD_HASHING=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "vulkan-headers", "spirv-headers", "spirv-tools-devel", "libxrandr-devel",
    "wayland-devel", "wayland-protocols",
]
pkgdesc = "Official Vulkan validation layers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/v{pkgver}.tar.gz"
sha256 = "3ee89f5f697658b3d5889089b26c4d9de1a7f2bd2acef4304f61a200835421f7"
# no test suite
options = ["!cross"]

@subpackage("vulkan-validationlayers-devel-static")
def _sdevel(self):
    return ["usr/lib/*.a"]

@subpackage("vulkan-validationlayers-devel")
def _devel(self):
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}",
        f"{pkgname}-devel-static={pkgver}-r{pkgrel}"
    ]
    return ["usr/include"]
