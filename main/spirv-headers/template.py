pkgname = "spirv-headers"
pkgver = "1.3.261.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "32b4c6ae6a2fa9b56c2c17233c8056da47e331f76e117729925825ea3e77a739"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
