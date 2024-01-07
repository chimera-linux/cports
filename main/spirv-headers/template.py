pkgname = "spirv-headers"
pkgver = "1.3.268.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "1022379e5b920ae21ccfb5cb41e07b1c59352a18c3d3fdcbf38d6ae7733384d4"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
