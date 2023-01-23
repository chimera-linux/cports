# note: some libs are unversioned (rebuild shaderc on updates)
pkgname = "glslang"
pkgver = "11.12.0"
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
sha256 = "7795a97450fecd9779f3d821858fbc2d1a3bf1dd602617d95b685ccbcabc302f"
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
