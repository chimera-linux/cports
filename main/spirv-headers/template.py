pkgname = "spirv-headers"
pkgver = "1.3.250.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/sdk-{pkgver}.tar.gz"
sha256 = "9d632a4dddd11f89a74a8c6f19cd29e8b0741d2fbb41ecc4dec26b922d28a2f3"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
