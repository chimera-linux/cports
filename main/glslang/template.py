# note: some libs are unversioned (rebuild shaderc on updates)
pkgname = "glslang"
pkgver = "12.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "python", "bison"]
checkdepends = ["bash"]
pkgdesc = "Khronos reference front-end for GLSL/ESSL + sample SPIR-V generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/KhronosGroup/glslang"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "870d17030fda7308c1521fb2e01a9e93cbe4b130bc8274e90d00e127432ab6f6"
# missing checkdepends
options = ["!check"]


@subpackage("glslang-progs")
def _progs(self):
    return self.default_progs()


@subpackage("glslang-devel")
def _devel(self):
    return [
        "usr/include",
        "usr/lib/libglslang.so",
        "usr/lib/cmake",
    ]
