pkgname = "spirv-headers"
pkgver = "1.3.224.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "c85714bfe62f84007286bd3b3c0471af0a7e06ab66bc2ca4623043011b28737f"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
