pkgname = "spirv-headers"
pkgver = "1.4.313.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "f68be549d74afb61600a1e3a7d1da1e6b7437758c8e77d664909f88f302c5ac1"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
