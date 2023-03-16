# note: some libs are unversioned (rebuild shaderc on updates)
pkgname = "glslang"
pkgver = "12.0.0"
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
sha256 = "7cb45842ec1d4b6ea775d624c3d2d8ba9450aa416b0482b0cc7e4fdd399c3d75"
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
