pkgname = "spirv-headers"
pkgver = "1.4.363.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "5b3a0d099f5c7649e29c0938476c462e71d66ad89a0bde42fa1ba3eb476956c9"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
