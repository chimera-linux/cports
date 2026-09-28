pkgname = "spirv-headers"
pkgver = "1.4.357.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "4d703067a7e06331ccb37bdfed3f9b7879cc61969a2689ae95c95db34a47ff07"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
