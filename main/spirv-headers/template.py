pkgname = "spirv-headers"
pkgver = "1.4.328.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "602364ab7bf404a7f352df7da5c645f1c4558a9c92616f8ee33422b04d5e35b7"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
