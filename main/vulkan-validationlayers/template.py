pkgname = "vulkan-validationlayers"
pkgver = "1.3.246"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DSPIRV_HEADERS_INSTALL_DIR=/usr",
    "-DGLSLANG_INSTALL_DIR=/usr",
    "-DBUILD_LAYER_SUPPORT_FILES=ON",
    "-DUSE_ROBIN_HOOD_HASHING=OFF",
    "-DBUILD_WERROR=OFF",
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
sha256 = "b6c37484d7e403d93af54e5c364e00537631250d784da2aaf8f85f45077f63ab"
hardening = ["!cfi"] # FIXME: inconsistent LTO unit splitting error
# no test suite
options = ["!cross", "!check"]

@subpackage("vulkan-validationlayers-devel-static")
def _sdevel(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]

@subpackage("vulkan-validationlayers-devel")
def _devel(self):
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}",
        f"{pkgname}-devel-static={pkgver}-r{pkgrel}"
    ]
    return ["usr/include"]
