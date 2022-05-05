pkgname = "spirv-headers"
pkgver = "1.3.211.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "30a78e61bd812c75e09fdc7a319af206b1044536326bc3e85fea818376a12568"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
