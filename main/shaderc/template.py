pkgname = "shaderc"
pkgver = "2024.0"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DSHADERC_SKIP_TESTS=ON",
    "-DSHADERC_SKIP_EXAMPLES=ON",
    "-DPYTHON_EXECUTABLE=python",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c761044e4e204be8e0b9a2d7494f08671ca35b92c4c791c7049594ca7514197f"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}
hardening = ["!cfi"]  # TODO


@subpackage("shaderc-progs")
def _progs(self):
    return self.default_progs()


@subpackage("shaderc-devel")
def _devel(self):
    return self.default_devel()
