pkgname = "shaderc"
pkgver = "2022.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSHADERC_SKIP_TESTS=ON", "-DSHADERC_SKIP_EXAMPLES=ON"]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c1dee49535cfdf86994990b21fe129a74bb0d628a647f4aae8905bd61df32607"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}
# FIXME probably no good
hardening = ["!vis"]

@subpackage("shaderc-progs")
def _progs(self):
    return self.default_progs()

@subpackage("shaderc-devel")
def _devel(self):
    return self.default_devel()
