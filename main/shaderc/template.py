pkgname = "shaderc"
pkgver = "2024.1"
pkgrel = 1
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
sha256 = "eb3b5f0c16313d34f208d90c2fa1e588a23283eed63b101edd5422be6165d528"
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
