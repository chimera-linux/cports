pkgname = "spirv-headers"
pkgver = "1.4.304.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "162b864ebaf339d66953fc2c4ad974bc4f453e0f04155cd3755a85e33f408eee"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
