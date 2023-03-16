pkgname = "spirv-headers"
pkgver = "1.3.239.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "fdaf6670e311cd1c08ae90bf813e89dd31630205bc60030ffd25fb0af39b51fe"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
