pkgname = "glslang"
pkgver = "13.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DALLOW_EXTERNAL_SPIRV_TOOLS=ON"]
hostmakedepends = ["cmake", "ninja", "python", "bison", "spirv-tools-devel"]
checkdepends = ["bash"]
pkgdesc = "Khronos reference front-end for GLSL/ESSL + sample SPIR-V generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/KhronosGroup/glslang"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "1c4d0a5a38c8aaf89a2d7e6093be734320599f5a6775b2726beeb05b0c054e66"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("glslang-progs")
def _progs(self):
    return self.default_progs()


@subpackage("glslang-devel")
def _devel(self):
    return self.default_devel()
