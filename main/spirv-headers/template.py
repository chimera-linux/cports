pkgname = "spirv-headers"
pkgver = "1.3.275.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "d46b261f1fbc5e85022cb2fada9a6facb5b0c9932b45007a77fe05639a605bd1"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
