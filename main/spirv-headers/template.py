pkgname = "spirv-headers"
pkgver = "1.3.250.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "442c3b329c0c1ef82a778c55b794410474c69bc08f8fb6cffaacf92c73af6f14"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
