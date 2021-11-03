# libraries are unversioned (abi breakage, rebuild shaderc on updates)
pkgname = "glslang"
pkgver = "8.13.3743"
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
sha256 = "639ebec56f1a7402f2fa094469a5ddea1eceecfaf2e9efe361376a0f73a7ee2f"
# missing checkdepends
options = ["!check"]

@subpackage("glslang-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/cmake",
    ]
