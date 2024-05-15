pkgname = "spirv-headers"
pkgver = "1.3.283.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "a68a25996268841073c01514df7bab8f64e2db1945944b45087e5c40eed12cb9"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
