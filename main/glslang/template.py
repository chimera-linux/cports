pkgname = "glslang"
pkgver = "16.5.0"
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
sha256 = "01af17195fbeb59e39e31e9506de35bb39dfd35807ea0c9a1a99d7d1183ddd45"
# stack overflow during check
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
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
