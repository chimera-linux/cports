pkgname = "spirv-headers"
pkgver = "1.3.243.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "16927b1868e7891377d059cd549484e4158912439cf77451ae7e01e2a3bcd28b"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
