pkgname = "shaderc"
pkgver = "2022.1"
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
sha256 = "592c0ba07706a940f95a24073d7f3d050daa0839f24019434a7b2776e5620ace"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}

@subpackage("shaderc-progs")
def _progs(self):
    return self.default_progs()

@subpackage("shaderc-devel")
def _devel(self):
    return self.default_devel()
