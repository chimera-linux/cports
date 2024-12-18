pkgname = "glslang"
pkgver = "15.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DALLOW_EXTERNAL_SPIRV_TOOLS=ON",
    "-DBUILD_SHARED_LIBS=ON",
    "-DGLSLANG_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "bison", "spirv-tools-devel"]
makedepends = ["gtest-devel"]
checkdepends = ["bash"]
pkgdesc = "Khronos reference front-end for GLSL/ESSL + sample SPIR-V generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/KhronosGroup/glslang"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "4bdcd8cdb330313f0d4deed7be527b0ac1c115ff272e492853a6e98add61b4bc"
# FIXME: tests reveal a suboverflow in TIntermConstantUnion::fold that should be fixed
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("glslang-progs")
def _(self):
    return self.default_progs()


@subpackage("glslang-devel")
def _(self):
    return self.default_devel()
