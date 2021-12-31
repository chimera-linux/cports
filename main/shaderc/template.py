pkgname = "shaderc"
pkgver = "2021.3"
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
sha256 = "d05f646c363e6447f233126b196238d9022a1dca1bf98f766511aa1a58320972"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}

@subpackage("shaderc-progs")
def _progs(self):
    return self.default_progs()

@subpackage("shaderc-devel")
def _devel(self):
    return self.default_devel()
