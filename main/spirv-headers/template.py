pkgname = "spirv-headers"
pkgver = "1.4.309.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "a96f8b4f2dfb18f7432e5c523e220ab0075372a9509e0c25fbff21c76af0de7c"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
