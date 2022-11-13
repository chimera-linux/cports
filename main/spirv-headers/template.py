pkgname = "spirv-headers"
pkgver = "1.3.231.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "fc340700b005e9a2adc98475b5afbbabd1bc931f789a2afd02d54ebc22522af3"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
