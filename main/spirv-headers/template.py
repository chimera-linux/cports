pkgname = "spirv-headers"
pkgver = "1.4.341.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "cab0a654c4917e16367483296b44cdb1d614e3120c721beafcd37e3a8580486c"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
