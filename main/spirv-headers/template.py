pkgname = "spirv-headers"
pkgver = "1.3.290.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "1b9ff8a33e07814671dee61fe246c67ccbcfc9be6581f229e251784499700e24"
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
