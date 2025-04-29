pkgname = "glslang"
pkgver = "15.3.0"
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
license = "BSD-3-Clause"
url = "https://github.com/KhronosGroup/glslang"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c6c21fe1873c37e639a6a9ac72d857ab63a5be6893a589f34e09a6c757174201"
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
