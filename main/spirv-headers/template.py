pkgname = "spirv-headers"
pkgver = "1.3.224.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "2fb1039ec6cec8943400e9b4d01d8bfe8c62a0bd1fafb7c39c56469aa247b838"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
