pkgname = "spirv-headers"
pkgver = "1.3.280.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "a00906b6bddaac1e37192eff2704582f82ce2d971f1aacee4d51d9db33b0f772"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
