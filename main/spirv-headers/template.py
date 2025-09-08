pkgname = "spirv-headers"
pkgver = "1.4.321.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "5bbea925663d4cd2bab23efad53874f2718248a73dcaf9dd21dff8cb48e602fc"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
