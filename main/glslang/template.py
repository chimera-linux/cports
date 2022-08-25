# note: some libs are unversioned (rebuild shaderc on updates)
pkgname = "glslang"
pkgver = "11.11.0"
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
sha256 = "26c216c3062512c018cbdd752224b8dad703b7e5bb90bf338ba2dbb5d4f11438"
# missing checkdepends
options = ["!check"]

@subpackage("glslang-progs")
def _progs(self):
    return self.default_progs()

@subpackage("glslang-devel-static")
def _static(self):
    self.depends = []
    return ["usr/lib/*.a"]

@subpackage("glslang-devel")
def _devel(self):
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        f"{pkgname}-devel-static={pkgver}-r{pkgrel}",
    ]
    return [
        "usr/include",
        "usr/lib/libglslang.so",
        "usr/lib/cmake",
    ]
